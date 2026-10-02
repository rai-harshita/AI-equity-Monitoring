import joblib
import pandas as pd

from fairlearn.metrics import (
    MetricFrame,
    selection_rate,
    demographic_parity_difference,
    equalized_odds_difference
)

from sklearn.metrics import accuracy_score, recall_score

from preprocessing import load_and_split_data

DATA_PATH = "data/loan_data_set.csv"
MODEL_PATH = "models/baseline_model.joblib"


def evaluate_gender_fairness():
    # Load original dataset
    df = pd.read_csv(DATA_PATH)

    # Use the same train/test split as the baseline model
    X_train, X_test, y_train, y_test = load_and_split_data()

    # Recover gender values for the test rows
    gender_test = df.loc[X_test.index, "Gender"]

    # Load trained model
    saved_model = joblib.load(MODEL_PATH)

    preprocessor = saved_model["preprocessor"]
    model = saved_model["model"]

    # Preprocess test data
    X_test_processed = preprocessor.transform(X_test)

    # Generate predictions
    predictions = model.predict(X_test_processed)

    # Remove cases where Gender is missing
    valid_mask = gender_test.notna()

    y_test_valid = y_test.loc[valid_mask]
    predictions_valid = predictions[valid_mask]
    gender_valid = gender_test.loc[valid_mask]

    # Calculate subgroup metrics
    metric_frame = MetricFrame(
        metrics={
            "accuracy": accuracy_score,
            "recall": recall_score,
            "selection_rate": selection_rate
        },
        y_true=y_test_valid,
        y_pred=predictions_valid,
        sensitive_features=gender_valid
    )

    print("===== GENDER FAIRNESS EVALUATION =====")

    print("\nSubgroup Metrics:")
    print(metric_frame.by_group)

    dp_difference = demographic_parity_difference(
        y_test_valid,
        predictions_valid,
        sensitive_features=gender_valid
    )

    eo_difference = equalized_odds_difference(
        y_test_valid,
        predictions_valid,
        sensitive_features=gender_valid
    )

    print("\nDemographic Parity Difference:")
    print(f"{dp_difference:.4f}")

    print("\nEqualized Odds Difference:")
    print(f"{eo_difference:.4f}")


def evaluate_education_fairness():
    # Load original dataset
    df = pd.read_csv(DATA_PATH)

    # Use the same train/test split as the baseline model
    X_train, X_test, y_train, y_test = load_and_split_data()

    # Recover education values for the test rows
    education_test = df.loc[X_test.index, "Education"]

    # Load trained model
    saved_model = joblib.load(MODEL_PATH)

    preprocessor = saved_model["preprocessor"]
    model = saved_model["model"]

    # Preprocess test data
    X_test_processed = preprocessor.transform(X_test)

    # Generate predictions
    predictions = model.predict(X_test_processed)

    # Remove cases where Education is missing
    valid_mask = education_test.notna()

    y_test_valid = y_test.loc[valid_mask]
    predictions_valid = predictions[valid_mask]
    education_valid = education_test.loc[valid_mask]

    # Calculate subgroup metrics
    metric_frame = MetricFrame(
        metrics={
            "accuracy": accuracy_score,
            "recall": recall_score,
            "selection_rate": selection_rate
        },
        y_true=y_test_valid,
        y_pred=predictions_valid,
        sensitive_features=education_valid
    )

    print("\n===== EDUCATION FAIRNESS EVALUATION =====")

    print("\nSubgroup Metrics:")
    print(metric_frame.by_group)

    dp_difference = demographic_parity_difference(
        y_test_valid,
        predictions_valid,
        sensitive_features=education_valid
    )

    eo_difference = equalized_odds_difference(
        y_test_valid,
        predictions_valid,
        sensitive_features=education_valid
    )

    print("\nDemographic Parity Difference:")
    print(f"{dp_difference:.4f}")

    print("\nEqualized Odds Difference:")
    print(f"{eo_difference:.4f}")


if __name__ == "__main__":
    evaluate_gender_fairness()
    evaluate_education_fairness()