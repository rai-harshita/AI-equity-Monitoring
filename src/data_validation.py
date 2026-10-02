import pandas as pd

DATA_PATH = "data/loan_data_set.csv"

REQUIRED_COLUMNS = [
    "Loan_ID",
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed",
    "ApplicantIncome",
    "CoapplicantIncome",
    "LoanAmount",
    "Loan_Amount_Term",
    "Credit_History",
    "Property_Area",
    "Loan_Status"
]

def validate_dataset(df):
    results = {
        "dataset_loaded": True,
        "required_columns_present": True,
        "duplicate_rows": 0,
        "missing_values": {},
        "invalid_target_values": [],
        "status": "PASS"
    }

    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        results["required_columns_present"] = False
        results["missing_columns"] = missing_columns
        results["status"] = "FAIL"

    results["duplicate_rows"] = int(df.duplicated().sum())

    missing_values = df.isnull().sum()
    results["missing_values"] = {
        column: int(value)
        for column, value in missing_values.items()
        if value > 0
    }

    if "Loan_Status" in df.columns:
        valid_targets = {"Y", "N"}
        invalid_targets = set(df["Loan_Status"].dropna().unique()) - valid_targets

        results["invalid_target_values"] = list(invalid_targets)

        if invalid_targets:
            results["status"] = "FAIL"

    return results


def print_validation_report(results):
    print("\n===== DATA VALIDATION REPORT =====")

    print("Dataset loaded:", results["dataset_loaded"])
    print("Required columns present:", results["required_columns_present"])
    print("Duplicate rows:", results["duplicate_rows"])

    print("\nMissing values:")
    if results["missing_values"]:
        for column, count in results["missing_values"].items():
            print(f"  {column}: {count}")
    else:
        print("  None")

    print("\nInvalid target values:")
    if results["invalid_target_values"]:
        print(" ", results["invalid_target_values"])
    else:
        print("  None")

    print("\nValidation status:", results["status"])


if __name__ == "__main__":
    df = pd.read_csv(DATA_PATH)

    validation_results = validate_dataset(df)

    print_validation_report(validation_results)