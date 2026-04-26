import pandas as pd
import json
import re

def checknan(value):
    if (value=="nan"):
        value=""
    return value

def generate_full_module(consumption_csv, output_file="functions_generated.py"):
    df = pd.read_csv(consumption_csv)

    categories = df["consumption"].tolist()

    food = df[df["category"].str.lower() == "food"]["consumption"].tolist()
    non_food = df[df["category"].str.lower() == "non_food"]["consumption"].tolist()

    with open(output_file, "w") as f:

        # =========================
        # HEADER
        # =========================
        f.write('"""\nAuto-generated VAT functions module\n"""\n\n')
        f.write("import numpy as np\n")
        f.write("from taxcalc.decorators import iterate_jit\n\n")

        # =========================
        # CONS FOOD
        # =========================
        args_food = [f"CONS_{c}" for c in food] + ["CONS_Food"]

        f.write("@iterate_jit(nopython=True)\n")
        f.write(f"def cal_CONS_Food({', '.join(args_food)}):\n")
        f.write("    CONS_Food = (\n")
        f.write(" +\n".join([f"        CONS_{c}" for c in food]))
        f.write("\n    )\n")
        f.write("    return CONS_Food\n\n")

        # =========================
        # CONS NON-FOOD
        # =========================
        args_nf = [f"CONS_{c}" for c in non_food] + ["CONS_Non_Food"]

        f.write("@iterate_jit(nopython=True)\n")
        f.write(f"def cal_CONS_Non_Food({', '.join(args_nf)}):\n")
        f.write("    CONS_Non_Food = (\n")
        f.write(" +\n".join([f"        CONS_{c}" for c in non_food]))
        f.write("\n    )\n")
        f.write("    return CONS_Non_Food\n\n")

        # =========================
        # CONS OTHER
        # =========================
        f.write("@iterate_jit(nopython=True)\n")
        f.write(f"def cal_CONS_Other({', '.join(args_nf[:-1])}, CONS_Other):\n")
        f.write("    CONS_Other = (\n")
        f.write(" +\n".join([f"        CONS_{c}" for c in non_food]))
        f.write("\n    )\n")
        f.write("    return CONS_Other\n\n")

        # =========================
        # CONS TOTAL
        # =========================
        f.write("@iterate_jit(nopython=True)\n")
        f.write("def cal_CONS_Total(CONS_Food, CONS_Other, CONS_Total):\n")
        f.write("    CONS_Total = CONS_Food + CONS_Other\n")
        f.write("    return CONS_Total\n\n")

        # =========================
        # ELASTICITY FUNCTIONS
        # =========================

        f.write("@iterate_jit(nopython=True)\n")
        f.write("def cal_Applicable_Elasticity_Food(\n")
        f.write("    elasticity_consumption_food_threshold,\n")
        f.write("    elasticity_consumption_food_value,\n")
        f.write("    CONS_Total,\n")
        f.write("    applicable_elasticity_food):\n")
        f.write("    elasticity_consumption_threshold0 = elasticity_consumption_food_threshold[0]\n")
        f.write("    elasticity_consumption_threshold1 = elasticity_consumption_food_threshold[1]\n")
        f.write("    elasticity_consumption_value0 = elasticity_consumption_food_value[0]\n")
        f.write("    elasticity_consumption_value1 = elasticity_consumption_food_value[1]\n")
        f.write("    elasticity_consumption_value2 = elasticity_consumption_food_value[2]\n")
        f.write("    if CONS_Total <= 0:\n")
        f.write("        applicable_elasticity_food = 0\n")
        f.write("    elif CONS_Total < elasticity_consumption_threshold0:\n")
        f.write("        applicable_elasticity_food = elasticity_consumption_value0\n")
        f.write("    elif CONS_Total < elasticity_consumption_threshold1:\n")
        f.write("        applicable_elasticity_food = elasticity_consumption_value1\n")
        f.write("    else:\n")
        f.write("        applicable_elasticity_food = elasticity_consumption_value2\n")
        f.write("    return applicable_elasticity_food\n\n")

        f.write("@iterate_jit(nopython=True)\n")
        f.write("def cal_Applicable_Elasticity_Non_Food(\n")
        f.write("    elasticity_consumption_non_food_threshold,\n")
        f.write("    elasticity_consumption_non_food_value,\n")
        f.write("    CONS_Total,\n")
        f.write("    applicable_elasticity_non_food):\n")
        f.write("    elasticity_consumption_threshold0 = elasticity_consumption_non_food_threshold[0]\n")
        f.write("    elasticity_consumption_threshold1 = elasticity_consumption_non_food_threshold[1]\n")
        f.write("    elasticity_consumption_value0 = elasticity_consumption_non_food_value[0]\n")
        f.write("    elasticity_consumption_value1 = elasticity_consumption_non_food_value[1]\n")
        f.write("    elasticity_consumption_value2 = elasticity_consumption_non_food_value[2]\n")
        f.write("    if CONS_Total <= 0:\n")
        f.write("        applicable_elasticity_non_food = 0\n")
        f.write("    elif CONS_Total < elasticity_consumption_threshold0:\n")
        f.write("        applicable_elasticity_non_food = elasticity_consumption_value0\n")
        f.write("    elif CONS_Total < elasticity_consumption_threshold1:\n")
        f.write("        applicable_elasticity_non_food = elasticity_consumption_value1\n")
        f.write("    else:\n")
        f.write("        applicable_elasticity_non_food = elasticity_consumption_value2\n")
        f.write("    return applicable_elasticity_non_food\n\n")

        # =========================
        # FOOD VAT
        # =========================
        f.write("@iterate_jit(nopython=True)\n")
        f.write("def cal_CONS_Food_behavior_and_vat(\n")

        for c in food:
            f.write(f"    rate_{c}, rate_{c}_curr_law,\n")
        for c in food:
            f.write(f"    CONS_{c},\n")

        f.write("    applicable_elasticity_food,\n")
        f.write("    vat_Food):\n")

        for c in food:
            f.write(
                f"    frac_change_of_consumption_{c} = applicable_elasticity_food * "
                f"((rate_{c} - rate_{c}_curr_law) / (1 + rate_{c}_curr_law))\n"
            )

        f.write("\n")

        for c in food:
            f.write(
                f"    CONS_{c}_behavior = CONS_{c} * "
                f"(1 + frac_change_of_consumption_{c})\n"
            )

        f.write("\n")

        for c in food:
            f.write(f"    vat_{c} = rate_{c} * CONS_{c}_behavior\n")

        f.write("\n")

        f.write("    vat_Food = (\n")
        f.write(" +\n".join([f"        vat_{c}" for c in food]))
        f.write("\n    )\n")

        f.write("    return vat_Food\n\n")

        # =========================
        # NON-FOOD VAT
        # =========================
        args = []
        for c in non_food:
            args.append(f"rate_{c}")
            args.append(f"rate_{c}_curr_law")
        for c in non_food:
            args.append(f"CONS_{c}")
        args += ["applicable_elasticity_non_food", "vat_Non_Food"]

        f.write("@iterate_jit(nopython=True)\n")
        f.write("def cal_CONS_Non_Food_behavior_and_vat(\n")
        for a in args:
            f.write(f"    {a},\n")
        f.write("):\n")

        for c in non_food:
            f.write(
                f"    frac_change_of_consumption_{c} = applicable_elasticity_non_food * "
                f"((rate_{c} - rate_{c}_curr_law) / (1 + rate_{c}_curr_law))\n"
            )

        f.write("\n")

        for c in non_food:
            f.write(
                f"    CONS_{c}_behavior = CONS_{c} * "
                f"(1 + frac_change_of_consumption_{c})\n"
            )

        f.write("\n")

        for c in non_food:
            f.write(f"    vat_{c} = rate_{c} * CONS_{c}_behavior\n")

        f.write("\n")

        f.write("    vat_Non_Food = (\n")
        f.write(" +\n".join([f"        vat_{c}" for c in non_food]))
        f.write("\n    )\n")

        f.write("    return vat_Non_Food\n\n")

        # =========================
        # TOTAL VAT
        # =========================
        f.write("@iterate_jit(nopython=True)\n")
        f.write("def cal_vat(vat_Food, vat_Non_Food, vatax):\n")
        f.write("    vatax = vat_Food + vat_Non_Food\n")
        f.write("    return vatax\n")

    print(f"✅ Full module generated: {output_file}")
    

def generate_function_list_from_file(py_file, output_json="functions_list.json"):
    with open(py_file, "r") as f:
        content = f.read()

    funcs = re.findall(r"def (cal_[A-Za-z0-9_]+)\(", content)

    func_list = {str(i): name for i, name in enumerate(funcs)}

    with open(output_json, "w") as f:
        json.dump(func_list, f, indent=4)

    print(f"✅ Extracted function list from {py_file}")

def generate_current_law_policy_input(consumption_csv, output_csv, tax_type, year):

    df = pd.read_csv(consumption_csv)

    rows = []

    def make_row(field_name, value, benchmark, col_var, min1, max1):
        return {
            "field_name": field_name,
            "long_name": f"{tax_type} for consumption of {field_name}",
            "description": f"{tax_type} for consumption of {field_name}",
            "itr_ref": f"{tax_type} Act",
            "notes": "",
            "row_var": "AYEAR",
            "row_label": year,
            "start_year": year,
            "cpi_inflatable": False,
            "cpi_inflated": False,
            "col_var": col_var,
            "col_label": "",
            "boolean_value": False,
            "integer_value": False,
            "value": value,
            "benchmark": benchmark,
            "range": "",
            "min": min1,
            "max": max1,
            "out_of_range_minmsg": "",
            "out_of_range_maxmsg": "",
            "out_of_range_action": "stop"
        }

    # =========================
    # VAT RATE PARAMETERS (FROM CSV)
    # =========================
    for _, r in df.iterrows():
        c = r["consumption"]
        rate = r["rate"]   # 👈 key change
        benchmark = r["benchmark"]
        rows.append(make_row(f"_rate_{c}", rate, benchmark, "", 0, 1))
        rows.append(make_row(f"_rate_{c}_curr_law", rate, benchmark, "", 0, 1))

    # =========================
    # ELASTICITY PARAMETERS
    # =========================
    rows.append(make_row("_elasticity_consumption_food_threshold", 0, "", "bracket", 0, 9e+99))
    rows.append(make_row("_elasticity_consumption_food_value", 0, "", "bracket", -100, 100))
    rows.append(make_row("_elasticity_consumption_non_food_threshold", 0, "", "bracket", 0, 9e+99))
    rows.append(make_row("_elasticity_consumption_non_food_value", 0, "", "bracket", -100, 100))

    # =========================
    # FINAL STRUCTURE
    # =========================
    cols = [
        "field_name", "long_name", "description", "itr_ref", "notes",
        "row_var", "row_label", "start_year", "cpi_inflatable", "cpi_inflated",
        "col_var", "col_label", "boolean_value", "integer_value", "value",
        "benchmark",
        "range", "min", "max",
        "out_of_range_minmsg", "out_of_range_maxmsg", "out_of_range_action"
    ]

    out_df = pd.DataFrame(rows)[cols]

    out_df.to_csv(output_csv, index=False)

    print(f"✅ Generated: {output_csv}")

    
def generate_current_law_policy(current_law_input_csv, current_law_policy_file):
        
    df = pd.read_csv(current_law_input_csv)
    final_json = {}
    cols = list(df.columns)
    for idx, row in df.iterrows():
        field_name=str(row['field_name'])
        print(field_name)
        item = {}
        item['long_name'] = str(row['long_name'])
        item['description'] = str(row['description'])
        item['itr_ref'] = str(row['itr_ref'])
        item['notes'] = checknan(str(row['notes']))
        item['row_var'] = str(row['row_var'])
        item['row_label'] = [str(int(row['row_label']))]
        item['start_year'] = int(row['start_year'])
        item['cpi_inflatable'] = row['cpi_inflatable']
        item['cpi_inflated'] = row['cpi_inflated']
        item['col_var'] = checknan(str(row['col_var']))
        if (field_name.find('elasticity')!=-1):
            item['col_label'] = ["bracket1", "bracket2", "bracket3"]
            if (field_name.find('threshold')!=-1):
                item['value'] = [[10000, 100000, 9e99]]
            elif (field_name.find('value')!=-1):
                if (field_name.find('food')!=-1):
                    item['value'] = [[0.0, 0.0, 0.0]]
                else:
                    item['value'] = [[0.0, 0.0, 0.0]]
        else:
            item['col_label'] = checknan(str(row['col_label']))
            item['value'] = [(row['value'])]
        item['boolean_value'] = row['boolean_value']
        item['integer_value'] = row['integer_value']
        range_dict = {}
        range_dict['min'] = row['min']
        range_dict['max'] = row['max']
        item['range']=range_dict
        item['out_of_range_minmsg'] = checknan(str(row['out_of_range_minmsg']))
        item['out_of_range_maxmsg'] = checknan(str(row['out_of_range_maxmsg']))
        item['out_of_range_action'] = str(row['out_of_range_action'])
        final_json[field_name]=item
    
    with open(current_law_policy_file, 'w') as f:
        json.dump(final_json, f, indent=4)
        
    print(f"JSON successfully written {final_json}")

def extract_calc_vars_from_py(functions_file):
    with open(functions_file, "r") as f:
        content = f.read()

    matches = re.findall(r"return\s+([A-Za-z_][A-Za-z0-9_]*)", content)

    # remove duplicates while preserving order
    seen = set()
    calc_vars = []
    for m in matches:
        if m not in seen:
            seen.add(m)
            calc_vars.append(m)

    return calc_vars

def generate_record_variables_input(consumption_csv, functions_file, year, output_csv):

    df = pd.read_csv(consumption_csv)
    year_col = str(int(year))
    
    rows = []

    # =========================
    # CORE REQUIRED VARIABLES (prepend)
    # =========================
    core_vars = [
        ("id_n", True, "int", "Unique positive numeric identifier for filing unit"),
        ("Year", True, "int", "Year"),
        ("weight", True, "float", "Weight"),
        ("CONS_Total", True, "float", "Weight"),
        ("CONS_Other", True, "float", "Weight"),  
        ("GROSS_INCOME", False, "float", "Weight")  
    ]

    for name, required, typ, desc in core_vars:
        rows.append({
            "field_category": "read",
            "field_name": name,
            "required": required,            
            "type": typ,
            "desc": desc,
            "form": "",
            year_col: year_col + " Household Survey",            
            "cross_year": "No",
            "attribute": "No"
        })
        
    # =========================
    # READ VARIABLES (inputs)
    # =========================
    for _, r in df.iterrows():
        c = r["consumption"]

        rows.append({
            "field_category": "read",
            "field_name": f"CONS_{c}",
            "required": False,            
            "type": "float",
            "desc": f"Consumption of {c}",
            "form": "",
            year_col: year_col + " Household Survey",            
            "cross_year": "No",
            "attribute": "No"
        })

    # =========================
    # CALC VARIABLES
    # =========================

    def get_description(var):
        if var.startswith("CONS_"):
            return f"{var.replace('_', ' ')}"
        elif var.startswith("vat_"):
            return f"VAT on {var.replace('vat_', '').replace('_', ' ')}"
        elif var == "vatax":
            return "Total VAT liability"
        else:
            return var
    
    calc_vars = extract_calc_vars_from_py(functions_file)
    calc_vars_with_desc = [(v, get_description(v)) for v in calc_vars]
    
    for name, desc in calc_vars_with_desc:
        rows.append({
            "field_category": "calc",
            "field_name": name,
            "required": False,
            "type": "float",
            "desc": desc,
            year_col: "Calculated by the Model",
            "cross_year": "",
            "attribute": ""
        })

    # =========================
    # FINAL STRUCTURE
    # =========================

    cols = [
        "field_category",
        "field_name",
        "required",
        "type",
        "desc",
        "form",
        year_col,
        "cross_year",
        "attribute"
    ]

    out_df = pd.DataFrame(rows)[cols]

    out_df.to_csv(output_csv, index=False)

    print(f"✅ Generated record variables CSV: {output_csv}")

def generate_record_variables_json(record_variables_input_csv, year, record_variables_json):
    df = pd.read_csv(record_variables_input_csv)
    
    final_json = {'read': {}, 'calc': {}}
    cols = list(df.columns)
    for idx, row in df.iterrows():
        print(row['field_category'])
        field_name=row['field_name']
        print(field_name)
        item = {}
        if (row['field_category']=='read'):
            item['required'] = row['required']
        item['type'] = str(row['type'])
        item['desc'] = str(row['desc'])
        #print(row['2015'])
        form = {}
        form[str(year)] = str(row[str(year)])
        item['form']=form
        if (row['field_category']=='read'):
            item['cross_year'] = str(row['cross_year'])
            item['attribute'] = str(row['attribute'])
        final_json[row['field_category']][field_name]=item
    
    with open(record_variables_json, 'w') as f:
        json.dump(final_json, f, indent=4)
    
    print(f"JSON successfully written {final_json}")

def generate_tax_incentives_benchmark_json(current_law_policy_input_csv, current_year, tax_incentives_benchmark_json):
        
    df = pd.read_csv(current_law_policy_input_csv)
    final_json = {}
    policy_json={}
    #cols = list(df.columns)
    
    for idx, row in df.iterrows():
        field_name=str(row['field_name'])
        if "elasticity" in field_name.lower():
            continue  # skip this row
        if "curr_law" in field_name.lower():
            continue  # skip this row
        item = {}
        year_item = str(int(current_year))
        item[year_item] = [(row['benchmark'])]    
        policy_json[field_name] = item
        
    final_json["policy"]=policy_json
    
    with open(tax_incentives_benchmark_json, 'w') as f:
        json.dump(final_json, f, indent=4)
        
    print(f"JSON successfully written {final_json}")

def generate_reform_input(current_law_policy_input_csv, reform_input_csv, current_year):

    df = pd.read_csv(current_law_policy_input_csv)

    rows = []

    for _, row in df.iterrows():
        field_name = str(row["field_name"])
        
        clean_name = field_name.lstrip("_")
        #  skip elasticity rows
        if "elasticity" in field_name.lower():
            continue
        if "curr_law" in field_name.lower():
            continue  # skip this row
            
        value = row["value"]

        rows.append({
            "Policy Parameter": clean_name,
            "Year": int(current_year),
            "Old_Value": value,
            "Value": value   # initial reform = current law
        })

    reform_df = pd.DataFrame(rows)

    reform_df.to_csv(reform_input_csv, index=False)

    print(f"✅ Reform input file generated: {reform_input_csv}")

def generate_growfactors(record_variables_input_csv,
                         gdp_csv,
                         growfactors_csv,
                         start_year,
                         end_year):

    df = pd.read_csv(record_variables_input_csv)

    # =========================
    # GET READ VARIABLES
    # =========================
    read_vars = df[df["field_category"] == "read"]["field_name"].tolist()
    read_vars = list(dict.fromkeys(read_vars))
    read_vars = [v for v in read_vars if v not in ["Year", "id_n", "weight"]]

    # =========================
    # LOAD GDP DATA
    # =========================
    gdp = pd.read_csv(gdp_csv)

    # 👉 adjust column names if needed
    # assume columns like: Year, GDP
    gdp = gdp.sort_values("Year")

    # create lookup dictionary
    gdp_dict = dict(zip(gdp["Year"], gdp["growth_rate"]))
    # =========================
    # DEFINE COLUMNS
    # =========================
    cols = ["Year", "CPI", "SALARY"] + read_vars

    rows = []

    # =========================
    # CREATE DATA
    # =========================
    for year in range(start_year, end_year + 1):
        row = {col: 1 for col in cols}
        row["Year"] = year
        rows.append(row)

    grow_df = pd.DataFrame(rows)[cols]

    # =========================
    # APPLY GDP GROWTH
    # =========================
    
    # map growth factor to each year
    grow_df["gf"] = grow_df["Year"].map(gdp_dict).fillna(1)
    
    # apply to ALL read_vars columns
    grow_df[read_vars] = grow_df[read_vars].multiply(grow_df["gf"], axis=0)
    
    # remove helper column
    grow_df.drop(columns="gf", inplace=True)
    
    # =========================
    # SAVE
    # =========================
    grow_df.to_csv(growfactors_csv, index=False)

    print(f"✅ Growfactors file generated: {growfactors_csv}")

tax_type = "VAT"
start_year = 2022
current_year = 2025
tax_expenditure_year = 2022
end_year = 2032
consumption_csv = "consumption_types.csv"
current_law_policy_input_csv = "current_law_policy_input1.csv"
generate_current_law_policy_input(consumption_csv, "current_law_policy_input1.csv", tax_type, year=start_year)
DEFAULTS_FILENAME = "current_law_policy_vat_bangladesh.json"
generate_current_law_policy(current_law_policy_input_csv, "taxcalc/"+DEFAULTS_FILENAME)

functions_file = "taxcalc/functions_vat_bangladesh.py"      
generate_full_module(consumption_csv, output_file=functions_file)

functions_names_file = "taxcalc/function_names_vat_bangladesh.json"  
generate_function_list_from_file(functions_file, output_json=functions_names_file)

record_variables_input_csv = "record_variables_input.csv"
generate_record_variables_input(consumption_csv, functions_file, start_year, record_variables_input_csv)
vat_records_variables_filename = "records_variables_vat_bangladesh.json"
generate_record_variables_json(record_variables_input_csv, start_year, "taxcalc/"+vat_records_variables_filename)


###
# IMPORTANT NOTE
# tax incentives benchmark is generated for all policy variables
# in case you don't want it for certain policy variables 
# include the exception in the function just as it is being 
# done for elasticity
###
tax_incentives_benchmark_json = "tax_incentives_benchmark_vat_bangladesh.json"
generate_tax_incentives_benchmark_json(current_law_policy_input_csv, tax_expenditure_year, tax_incentives_benchmark_json)

reform_input_csv = "reform_input2.csv"
generate_reform_input(current_law_policy_input_csv, reform_input_csv, current_year)

growfactors_csv = "taxcalc/growfactors_vat_bangladesh.csv"
gdp_csv = "gdp_nominal_bangladesh.csv"
generate_growfactors(record_variables_input_csv, gdp_csv, growfactors_csv, start_year, end_year)

    

