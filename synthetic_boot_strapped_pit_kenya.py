import numpy as np
import pandas as pd

# ============================================================
# SETTINGS
# ============================================================
INPUT_FILE = "taxcalc/pit_kenya.csv"          # change path if needed
OUTPUT_FILE = "taxcalc/synthetic_bootstrap_pit_kenya.csv"
WEIGHTS_FILE = "taxcalc/synthetic_bootstrap_pit_weights_kenya.csv"
N_SYNTH = 100_000
RANDOM_SEED = 27

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

# ============================================================
# LOAD DATA
# ============================================================
df = pd.read_csv(INPUT_FILE)

required_cols = TARGET_COLS + [WEIGHT_COL]
missing = [c for c in required_cols if c not in df.columns]
if missing:
    raise ValueError(f"Missing required columns: {missing}")

df = df[required_cols].copy()

# Make sure columns are numeric
for c in TARGET_COLS + [WEIGHT_COL]:
    df[c] = pd.to_numeric(df[c], errors="coerce")

# Drop rows with missing or nonpositive weights
df = df[df[WEIGHT_COL].notna() & (df[WEIGHT_COL] > 0)].copy()

# Fill missing target values conservatively
for c in TARGET_COLS:
    if c == "is_disabled":
        df[c] = df[c].fillna(0)
        df[c] = (df[c] > 0).astype(int)
    else:
        df[c] = df[c].fillna(0)

# ============================================================
# WEIGHTED BOOTSTRAP
# ============================================================
rng = np.random.default_rng(RANDOM_SEED)

weights = df[WEIGHT_COL].to_numpy(dtype=float)
prob = weights / weights.sum()

sample_idx = rng.choice(
    df.index.to_numpy(),
    size=N_SYNTH,
    replace=True,
    p=prob
)

synthetic = df.loc[sample_idx, TARGET_COLS].reset_index(drop=True)

# Assign equal weights to synthetic rows
synthetic["weight"] = 1.0

# ============================================================
# OPTIONAL: SMALL JITTER FOR CONTINUOUS VARIABLES
# ============================================================
# This makes the synthetic data less like exact copies of original rows.
# Set APPLY_JITTER = False if you want pure bootstrap only.
APPLY_JITTER = True

continuous_cols = [
    "emp_income",
    "interest_income",
    "business_income",
    "mortage_interest",
    "home_own_saving_plan_dep",
    "pension_contribution",
    "hosp_tot_deposit_year",
    "insurance_relief"
]

if APPLY_JITTER:
    for c in continuous_cols:
        x = synthetic[c].to_numpy(dtype=float)

        # Add tiny noise only to positive values
        positive = x > 0
        if positive.any():
            # Use 1% of std as jitter scale
            std_c = df[c].std()
            jitter_scale = 0.01 * std_c if pd.notna(std_c) and std_c > 0 else 0.0

            if jitter_scale > 0:
                noise = rng.normal(loc=0.0, scale=jitter_scale, size=positive.sum())
                x[positive] = np.maximum(0, x[positive] + noise)

        synthetic[c] = x

# Ensure binary stays binary
synthetic["is_disabled"] = synthetic["is_disabled"].astype(int)
synthetic["is_disabled"] = (synthetic["is_disabled"] > 0).astype(int)

# ============================================================
# SAVE DATA FILE AND WEIGHTS FILE
# ============================================================
synthetic['id_n']=synthetic.index
synthetic['Year']=2023
synthetic.to_csv(OUTPUT_FILE, index=False)

df_weight = synthetic[['weight']].copy()

df_weight.columns = ['WT2023']
df_weight['WT2024'] = df_weight['WT2023']
df_weight['WT2025'] = df_weight['WT2023']
df_weight['WT2026'] = df_weight['WT2023']
df_weight['WT2027'] = df_weight['WT2023']
df_weight['WT2028'] = df_weight['WT2023']
df_weight['WT2029'] = df_weight['WT2023']
df_weight['WT2030'] = df_weight['WT2023']
df_weight['WT2031'] = df_weight['WT2023']
df_weight['WT2032'] = df_weight['WT2023']

df_weight.to_csv(WEIGHTS_FILE, index=False)
# ============================================================
# QUICK VALIDATION
# ============================================================
def weighted_mean(x, w):
    x = np.asarray(x, dtype=float)
    w = np.asarray(w, dtype=float)
    return np.sum(x * w) / np.sum(w)

print("Synthetic dataset created.")
print(f"Output file: {OUTPUT_FILE}")
print(f"Synthetic rows: {len(synthetic):,}")
print(f"Original rows used: {len(df):,}")
print(f"All synthetic weights equal? {synthetic['weight'].nunique() == 1}")

print("\nComparison: weighted original mean vs synthetic mean")
for c in TARGET_COLS:
    orig_mean = weighted_mean(df[c].to_numpy(dtype=float), weights)
    syn_mean = synthetic[c].mean()
    print(f"{c:28s} original={orig_mean:,.2f}   synthetic={syn_mean:,.2f}")
    print(f"{c:28s} difference (%)={(orig_mean-syn_mean)*100/orig_mean:,.2f}")

# ============================================================
# CALIBRATION
# ============================================================

# reweight using tax projections calibrated
tax_collection_2023_24_billion = 543.186
# synthetic data has only 100,000 observations
tax_collection_model_billion_2023 = 22.99
multiplicative_factor_2023 = tax_collection_2023_24_billion/tax_collection_model_billion_2023

# reweight using tax projections calibrated
tax_collection_2024_25_billion = 560.945
# synthetic data has only 100,000 observations
tax_collection_model_billion_2024 = 26.76
multiplicative_factor_2024 = tax_collection_2024_25_billion/tax_collection_model_billion_2024


pit_synthetic = pd.read_csv(OUTPUT_FILE)
pit_synthetic['weight'] = multiplicative_factor_2023*pit_synthetic['weight']
pit_synthetic.to_csv(OUTPUT_FILE, index=False)

df_weight = pd.read_csv(WEIGHTS_FILE)
                 
df_weight['WT2023'] = multiplicative_factor_2023*df_weight['WT2023']
df_weight['WT2024'] = multiplicative_factor_2024*df_weight['WT2024']
df_weight['WT2025'] = df_weight['WT2024']
df_weight['WT2026'] = df_weight['WT2024']
df_weight['WT2027'] = df_weight['WT2024']
df_weight['WT2028'] = df_weight['WT2024']
df_weight['WT2029'] = df_weight['WT2024']
df_weight['WT2030'] = df_weight['WT2024']
df_weight['WT2031'] = df_weight['WT2024']
df_weight['WT2032'] = df_weight['WT2024']
df_weight.to_csv(WEIGHTS_FILE, index=False)
