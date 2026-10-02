import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

from preprocessing import load_and_split_data

MODEL_PATH = "models/baseline_model.joblib"


def evaluate_model():
    X_train, X_test, y_train, y_test = load_and_split_data()

    saved_model = joblib.load(MODEL_PATH)

    preprocessor = saved_model["preprocessor"]
    model = saved_model["model"]

    X_test_processed = preprocessor.transform(X_test)

    predictions = model.predict(X_test_processed)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)

    matrix = confusion_matrix(y_test, predictions)

    print("===== BASELINE MODEL EVALUATION =====")
    print("Model: Logistic Regression")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")

    print("\nConfusion Matrix:")
    print(matrix)


if __name__ == "__main__":
    evaluate_model()