import json

BASELINE_PATH = "reports/baseline_metrics.json"
GENDER_PATH = "reports/gender_fairness_metrics.json"
EDUCATION_PATH = "reports/education_fairness_metrics.json"
EXPLAINABILITY_PATH = "reports/explainability_results.json"
GENAI_PATH = "reports/genai_safety_results.json"

OUTPUT_PATH = "reports/governance_decision.json"


def load_json(path):
    with open(path, "r") as file:
        return json.load(file)


def evaluate_fairness(fairness_data):
    metrics = fairness_data["fairness_metrics"]

    dp_difference = metrics["demographic_parity_difference"]
    eo_difference = metrics["equalized_odds_difference"]

    return {
        "demographic_parity_difference": dp_difference,
        "equalized_odds_difference": eo_difference,
        "requires_review": dp_difference > 0.10 or eo_difference > 0.10
    }


def evaluate_genai_safety(genai_data):
    summary = genai_data["summary"]

    return {
        "total_cases": summary["total_cases"],
        "passed_cases": summary["passed_cases"],
        "failed_cases": summary["failed_cases"],
        "pass_rate": summary["pass_rate"],
        "requires_review": summary["failed_cases"] > 0
    }


def generate_governance_decision():
    baseline = load_json(BASELINE_PATH)
    gender = load_json(GENDER_PATH)
    education = load_json(EDUCATION_PATH)
    explainability = load_json(EXPLAINABILITY_PATH)
    genai = load_json(GENAI_PATH)

    gender_result = evaluate_fairness(gender)
    education_result = evaluate_fairness(education)
    genai_result = evaluate_genai_safety(genai)

    fairness_review = (
        gender_result["requires_review"]
        or education_result["requires_review"]
    )

    explanation_available = len(
        explainability.get("top_features", [])
    ) > 0

    performance_available = all(
        metric in baseline
        for metric in [
            "accuracy",
            "precision",
            "recall",
            "f1_score"
        ]
    )

    if not performance_available:
        overall_status = "INCOMPLETE"
    elif genai_result["requires_review"]:
        overall_status = "REVIEW"
    elif fairness_review:
        overall_status = "REVIEW"
    elif not explanation_available:
        overall_status = "REVIEW"
    else:
        overall_status = "PASS"

    decision = {
        "overall_status": overall_status,
        "performance": {
            "accuracy": baseline["accuracy"],
            "precision": baseline["precision"],
            "recall": baseline["recall"],
            "f1_score": baseline["f1_score"]
        },
        "fairness": {
            "Gender": gender_result,
            "Education": education_result
        },
        "explainability": {
            "available": explanation_available,
            "top_features_count": len(
                explainability.get("top_features", [])
            )
        },
        "genai_safety": genai_result,
        "governance_actions": []
    }

    if fairness_review:
        decision["governance_actions"].append(
            "Review subgroup fairness metrics and investigate observed differences."
        )

    if genai_result["requires_review"]:
        decision["governance_actions"].append(
            "Review failed GenAI safety cases before deployment."
        )

    if not explanation_available:
        decision["governance_actions"].append(
            "Provide explainability evidence before deployment."
        )

    if not decision["governance_actions"]:
        decision["governance_actions"].append(
            "Continue monitoring performance, fairness and safety after deployment."
        )

    with open(OUTPUT_PATH, "w") as file:
        json.dump(decision, file, indent=4)

    print("===== GOVERNANCE DECISION =====")
    print("Overall status:", overall_status)

    print("\nGovernance actions:")

    for action in decision["governance_actions"]:
        print("-", action)

    print("\nGovernance decision saved to:", OUTPUT_PATH)


if __name__ == "__main__":
    generate_governance_decision()