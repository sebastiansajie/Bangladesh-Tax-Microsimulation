import numpy as np
import pandas as pd
from scipy.stats import norm

# ============================================================
# SETTINGS
# ============================================================
INPUT_FILE = "taxcalc/pit_kenya.csv"          # change path if needed
OUTPUT_FILE = "synthetic_pit_kenya.csv"
N_SYNTH = 100000
RANDOM_SEED = 42

TARGET_COLS = [
    "emp_income",
    "interest_income",
    "business_income",
    "mortage_interest",
    "home_own_saving_plan_dep",
    "pension_contribution",
    "hosp_tot_deposit_year",
    "is_disabled",
    "insurance_relief"
]

WEIGHT_COL = "weight"
BINARY_COLS = ["is_disabled"]
CONT_COLS = [c for c in TARGET_COLS if c not in BINARY_COLS]

# ============================================================
# HELPER FUNCTIONS
# ============================================================
def weighted_quantile(values, quantiles, sample_weight=None):
    """
    Weighted quantile function.
    values: 1D array
    quantiles: array-like in [0,1]
    sample_weight: 1D array of weights
    """
    values = np.asarray(values, dtype=float)
    quantiles = np.asarray(quantiles)

    if sample_weight is None:
        sample_weight = np.ones(len(values), dtype=float)
    else:
        sample_weight = np.asarray(sample_weight, dtype=float)

    mask = np.isfinite(values) & np.isfinite(sample_weight) & (sample_weight > 0)
    values = values[mask]
    sample_weight = sample_weight[mask]

    sorter = np.argsort(values)
    values = values[sorter]
    sample_weight = sample_weight[sorter]

    cumulative_weight = np.cumsum(sample_weight)
    cumulative_weight = cumulative_weight / cumulative_weight[-1]

    return np.interp(quantiles, cumulative_weight, values)


def weighted_mean(x, w):
    x = np.asarray(x, dtype=float)
    w = np.asarray(w, dtype=float)
    return np.sum(w * x) / np.sum(w)


def weighted_cov(x, y, w):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    w = np.asarray(w, dtype=float)

    mx = weighted_mean(x, w)
    my = weighted_mean(y, w)
    return np.sum(w * (x - mx) * (y - my)) / np.sum(w)


def weighted_corr_matrix(X, w):
    """
    X: 2D numpy array (n, p)
    w: 1D weights
    returns p x p weighted correlation matrix
    """
    p = X.shape[1]
    corr = np.eye(p)

    for i in range(p):
        for j in range(i + 1, p):
            cov_ij = weighted_cov(X[:, i], X[:, j], w)
            var_i = weighted_cov(X[:, i], X[:, i], w)
            var_j = weighted_cov(X[:, j], X[:, j], w)

            if var_i <= 0 or var_j <= 0:
                rho = 0.0
            else:
                rho = cov_ij / np.sqrt(var_i * var_j)

            rho = np.clip(rho, -0.999, 0.999)
            corr[i, j] = rho
            corr[j, i] = rho

    return corr


def nearest_positive_definite(A, epsilon=1e-8):
    """
    Make correlation/covariance matrix positive definite if needed.
    """
    B = (A + A.T) / 2
    eigvals, eigvecs = np.linalg.eigh(B)
    eigvals[eigvals < epsilon] = epsilon
    B_pd = eigvecs @ np.diag(eigvals) @ eigvecs.T

    # rescale to correlation matrix
    d = np.sqrt(np.diag(B_pd))
    B_corr = B_pd / np.outer(d, d)
    np.fill_diagonal(B_corr, 1.0)
    return B_corr


def weighted_midrank_cdf(x, w):
    """
    Returns weighted empirical CDF values in (0,1), using weighted mid-ranks.
    """
    x = np.asarray(x, dtype=float)
    w = np.asarray(w, dtype=float)

    sorter = np.argsort(x)
    x_sorted = x[sorter]
    w_sorted = w[sorter]

    cum_w = np.cumsum(w_sorted)
    total_w = cum_w[-1]

    # mid-point CDF
    u_sorted = (cum_w - 0.5 * w_sorted) / total_w

    u = np.empty_like(u_sorted)
    u[sorter.argsort()] = u_sorted

    # clip away from 0 and 1
    eps = 1e-6
    u = np.clip(u, eps, 1 - eps)
    return u


# ============================================================
# LOAD DATA
# ============================================================
np.random.seed(RANDOM_SEED)

df = pd.read_csv(INPUT_FILE)

required_cols = TARGET_COLS + [WEIGHT_COL]
missing = [c for c in required_cols if c not in df.columns]
if missing:
    raise ValueError(f"Missing required columns: {missing}")

# Keep only needed columns
df = df[required_cols].copy()

# Clean weights
df[WEIGHT_COL] = pd.to_numeric(df[WEIGHT_COL], errors="coerce")
df = df[df[WEIGHT_COL].notna() & (df[WEIGHT_COL] > 0)].copy()

# Coerce variables to numeric
for c in TARGET_COLS:
    df[c] = pd.to_numeric(df[c], errors="coerce")

# Fill missing values conservatively
for c in CONT_COLS:
    df[c] = df[c].fillna(0)

for c in BINARY_COLS:
    df[c] = df[c].fillna(0).astype(int)
    df[c] = (df[c] > 0).astype(int)

w = df[WEIGHT_COL].to_numpy(dtype=float)

# ============================================================
# STEP 1: PREPARE LATENT NORMAL REPRESENTATION
# ============================================================
# Continuous variables:
# - preserve zeros explicitly
# - for positive values, use log1p and weighted empirical CDF -> normal scores
latent_cols = []
latent_data = {}

positive_models = {}   # store weighted quantile maps for inverse transform
zero_probs = {}        # store weighted zero probabilities

for c in CONT_COLS:
    x = df[c].to_numpy(dtype=float)
    x = np.maximum(x, 0)

    is_zero = (x <= 0)
    p_zero = np.sum(w[is_zero]) / np.sum(w)
    zero_probs[c] = p_zero

    # latent variable for copula estimation
    # give zeros a low uniform band, positives an upper band
    u = np.empty(len(x), dtype=float)

    if p_zero >= 1.0:
        # all zero
        u[:] = 0.5
        positive_models[c] = None
    else:
        pos = ~is_zero
        x_pos = np.log1p(x[pos])

        # weighted midrank among positive values only
        u_pos_inner = weighted_midrank_cdf(x_pos, w[pos])

        # map positives to interval (p_zero, 1)
        u[pos] = p_zero + (1 - p_zero) * u_pos_inner

        # zeros occupy the lower interval (0, p_zero)
        if p_zero > 0:
            rng = np.random.default_rng(RANDOM_SEED)
            u[is_zero] = rng.uniform(low=1e-6, high=max(p_zero - 1e-6, 2e-6), size=is_zero.sum())
        else:
            u[is_zero] = 1e-6

        positive_models[c] = {
            "log_positive_values": x_pos,
            "positive_weights": w[pos]
        }

    u = np.clip(u, 1e-6, 1 - 1e-6)
    z = norm.ppf(u)

    latent_cols.append(c)
    latent_data[c] = z

# Binary variable(s): map observed proportion to latent threshold
for c in BINARY_COLS:
    x = df[c].to_numpy(dtype=int)
    p1 = np.sum(w[x == 1]) / np.sum(w)
    p1 = np.clip(p1, 1e-6, 1 - 1e-6)

    # assign latent scores using two normal regions
    # 0 -> below threshold, 1 -> above threshold
    threshold = norm.ppf(1 - p1)

    rng = np.random.default_rng(RANDOM_SEED + 123)
    u = np.empty(len(x), dtype=float)
    u[x == 0] = rng.uniform(1e-6, max((1 - p1) - 1e-6, 2e-6), size=(x == 0).sum())
    u[x == 1] = rng.uniform(min((1 - p1) + 1e-6, 1 - 2e-6), 1 - 1e-6, size=(x == 1).sum())

    z = norm.ppf(u)

    latent_cols.append(c)
    latent_data[c] = z

# Build latent matrix
Z = np.column_stack([latent_data[c] for c in latent_cols])

# ============================================================
# STEP 2: FIT WEIGHTED CORRELATION IN LATENT SPACE
# ============================================================
corr = weighted_corr_matrix(Z, w)
corr = nearest_positive_definite(corr)

# ============================================================
# STEP 3: GENERATE SYNTHETIC LATENT NORMAL DATA
# ============================================================
rng = np.random.default_rng(RANDOM_SEED)
Z_syn = rng.multivariate_normal(
    mean=np.zeros(len(latent_cols)),
    cov=corr,
    size=N_SYNTH
)

U_syn = norm.cdf(Z_syn)
U_syn = np.clip(U_syn, 1e-6, 1 - 1e-6)

# ============================================================
# STEP 4: INVERSE TRANSFORM TO ORIGINAL SCALE
# ============================================================
syn = pd.DataFrame(index=np.arange(N_SYNTH))

# Continuous variables
for j, c in enumerate(latent_cols):
    if c in CONT_COLS:
        u = U_syn[:, j]
        p_zero = zero_probs[c]

        x_syn = np.zeros(N_SYNTH, dtype=float)

        positive_model = positive_models[c]
        if positive_model is None:
            x_syn[:] = 0.0
        else:
            is_pos = u > p_zero

            if is_pos.any():
                # rescale u from (p_zero,1) to (0,1) for positive values
                u_pos = (u[is_pos] - p_zero) / max(1 - p_zero, 1e-12)
                u_pos = np.clip(u_pos, 1e-6, 1 - 1e-6)

                log_pos_values = positive_model["log_positive_values"]
                pos_weights = positive_model["positive_weights"]

                log_x = weighted_quantile(log_pos_values, u_pos, pos_weights)
                x_syn[is_pos] = np.expm1(log_x)

            x_syn[~is_pos] = 0.0

        # keep nonnegative
        x_syn = np.maximum(x_syn, 0.0)
        syn[c] = x_syn

# Binary variables
for j, c in enumerate(latent_cols):
    if c in BINARY_COLS:
        x = df[c].to_numpy(dtype=int)
        p1 = np.sum(w[x == 1]) / np.sum(w)
        threshold = norm.ppf(1 - np.clip(p1, 1e-6, 1 - 1e-6))

        syn[c] = (Z_syn[:, j] > threshold).astype(int)

# equal synthetic weights by default
syn["weight"] = 1.0

# reorder columns
syn = syn[TARGET_COLS + ["weight"]]

# ============================================================
# STEP 5: SAVE
# ============================================================
syn.to_csv(OUTPUT_FILE, index=False)

# ============================================================
# STEP 6: QUICK VALIDATION
# ============================================================
def weighted_mean_series(x, w):
    return np.sum(x * w) / np.sum(w)

print("\nSynthetic dataset created.")
print(f"Output file: {OUTPUT_FILE}")
print(f"Number of synthetic rows: {len(syn):,}")

print("\nOriginal data rows:", f"{len(df):,}")
print("Original unique weights:", df["weight"].nunique())

print("\nComparison of weighted original means vs synthetic means:")
for c in TARGET_COLS:
    if c == "is_disabled":
        orig_mean = weighted_mean_series(df[c].to_numpy(dtype=float), w)
        syn_mean = syn[c].mean()
        print(f"{c:28s} original={orig_mean:.6f}   synthetic={syn_mean:.6f}")
    else:
        orig_mean = weighted_mean_series(df[c].to_numpy(dtype=float), w)
        syn_mean = syn[c].mean()
        print(f"{c:28s} original={orig_mean:,.2f}   synthetic={syn_mean:,.2f}")

print("\nDone.")
