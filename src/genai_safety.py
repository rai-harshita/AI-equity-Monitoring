import json

INPUT_PATH = "tests/genai_safety_cases.json"
OUTPUT_PATH = "reports/genai_safety_results.json"


def evaluate_case(case):
    category = case["category"]
    risk_level = case["risk_level"]

    if risk_level == "HIGH":
        decision = "BLOCK"
        reason = "High-risk request requires prevention."
    elif category in {"incomplete", "ambiguous"}:
        decision = "REVIEW"
        reason = "Insufficient or ambiguous information requires human review."
    else:
        decision = "SAFE"
        reason = "Request is within the defined low-risk safety scope."

    return {
        "case_id": case["case_id"],
        "category": category,
        "risk_level": risk_level,
        "expected_status": case["expected_status"],
        "actual_status": decision,
        "reason": reason,
        "match": decision == case["expected_status"]
    }


def run_safety_evaluation():
    with open(INPUT_PATH, "r") as file:
        cases = json.load(file)

    results = []

    for case in cases:
        results.append(evaluate_case(case))

    total_cases = len(results)
    passed_cases = sum(result["match"] for result in results)

    summary = {
        "total_cases": total_cases,
        "passed_cases": passed_cases,
        "failed_cases": total_cases - passed_cases,
        "pass_rate": passed_cases / total_cases if total_cases else 0
    }

    output = {
        "summary": summary,
        "results": results
    }

    with open(OUTPUT_PATH, "w") as file:
        json.dump(output, file, indent=4)

    print("===== GENAI SAFETY EVALUATION =====")
    print("Total cases:", total_cases)
    print("Passed cases:", passed_cases)
    print("Failed cases:", total_cases - passed_cases)
    print(f"Pass rate: {summary['pass_rate']:.2%}")

    print("\nCase Results:")

    for result in results:
        print(
            f"{result['case_id']}: "
            f"{result['actual_status']} "
            f"({'PASS' if result['match'] else 'FAIL'})"
        )

    print("\nResults saved to:", OUTPUT_PATH)


if __name__ == "__main__":
    run_safety_evaluation()