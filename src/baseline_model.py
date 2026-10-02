import joblib
from sklearn.linear_model import LogisticRegression

from preprocessing import load_and_split_data, create_preprocessor

MODEL_PATH = "models/baseline_model.joblib"


def train_baseline_model():
    X_train, X_test, y_train, y_test = load_and_split_data()

    preprocessor = create_preprocessor()

    model = LogisticRegression(
    max_iter=5000,
    random_state=42
)

    pipeline = preprocessor

    X_train_processed = pipeline.fit_transform(X_train)
    X_test_processed = pipeline.transform(X_test)

    model.fit(X_train_processed, y_train)

    joblib.dump(
        {
            "preprocessor": pipeline,
            "model": model
        },
        MODEL_PATH
    )

    print("===== BASELINE MODEL =====")
    print("Model: Logistic Regression")
    print("Training rows:", len(X_train))
    print("Testing rows:", len(X_test))
    print("Model saved to:", MODEL_PATH)

    return model, X_test_processed, y_test


if __name__ == "__main__":
    train_baseline_model()