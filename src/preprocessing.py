import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

DATA_PATH = "data/loan_data_set.csv"

TARGET = "Loan_Status"

NUMERIC_COLUMNS = [
    "ApplicantIncome",
    "CoapplicantIncome",
    "LoanAmount",
    "Loan_Amount_Term",
    "Credit_History"
]

CATEGORICAL_COLUMNS = [
    "Married",
    "Dependents",
    "Self_Employed",
    "Property_Area"
]


def load_and_split_data():
    df = pd.read_csv(DATA_PATH)

    X = df.drop(columns=[TARGET, "Loan_ID", "Gender", "Education"])
    y = df[TARGET].map({"N": 0, "Y": 1})

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    return X_train, X_test, y_train, y_test


def create_preprocessor():
    numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer([
        ("numeric", numeric_pipeline, NUMERIC_COLUMNS),
        ("categorical", categorical_pipeline, CATEGORICAL_COLUMNS)
    ])

    return preprocessor


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_and_split_data()

    print("===== PREPROCESSING CHECK =====")
    print("Training rows:", len(X_train))
    print("Testing rows:", len(X_test))
    print("Training target distribution:")
    print(y_train.value_counts())
    print("Testing target distribution:")
    print(y_test.value_counts())

    preprocessor = create_preprocessor()

    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    print("\nProcessed training shape:", X_train_processed.shape)
    print("Processed testing shape:", X_test_processed.shape)