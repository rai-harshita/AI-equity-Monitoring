import joblib
import json
import numpy as np
import pandas as pd
import shap

from preprocessing import load_and_split_data

MODEL_PATH = "models/baseline_model.joblib"
OUTPUT_PATH = "reports/explainability_results.json"


def run_explainability():
    X_train, X_test, y_train, y_test = load_and_split_data()

    saved_model = joblib.load(MODEL_PATH)

    preprocessor = saved_model["preprocessor"]
    model = saved_model["model"]

    X_train_processed = preprocessor.transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    feature_names = preprocessor.get_feature_names_out()

    X_train_processed = preprocessor.transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    X_test_df = pd.DataFrame(
        X_test_processed,
        columns=feature_names
    )

    background = shap.sample(
        X_train_processed,
        100,
        random_state=42
    )

    explainer = shap.Explainer(
        model,
        background,
        feature_names=feature_names
    )

    shap_values = explainer(X_test_df)

    mean_abs_shap = np.abs(shap_values.values).mean(axis=0)

    feature_importance = pd.DataFrame({
        "feature": feature_names,
        "mean_absolute_shap": mean_abs_shap
    })

    feature_importance = feature_importance.sort_values(
        "mean_absolute_shap",
        ascending=False
    )

    print("===== SHAP EXPLAINABILITY =====")

    print("\nTop 10 Features:")
    print(feature_importance.head(10).to_string(index=False))

    results = {
        "method": "SHAP",
        "model": "Logistic Regression",
        "test_samples": len(X_test),
        "top_features": [
            {
                "feature": row["feature"],
                "mean_absolute_shap": float(row["mean_absolute_shap"])
            }
            for _, row in feature_importance.head(10).iterrows()
        ]
    }

    with open(OUTPUT_PATH, "w") as file:
        json.dump(results, file, indent=4)

    print("\nExplainability results saved to:", OUTPUT_PATH)


if __name__ == "__main__":
    run_explainability()