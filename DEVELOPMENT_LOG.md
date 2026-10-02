# Development Log

## 10 September 2026

### Work Completed – Project Setup

- Created GitHub repository for the project.
- Created the local project folder and opened it in Visual Studio Code.
- Verified Python installation.
- Created and activated a Python virtual environment.
- Created the requirements file.
- Installed the required Python libraries.
- Created the initial project directory structure.
- Configured the `.gitignore` file.

### Learning

- Learned how Python virtual environments isolate project dependencies.
- Learned how a requirements file helps manage project libraries.
- Learned the basic structure of a modular Python project.

### Challenges

- The `python` command was not initially recognized, so the Python launcher command `py` was used.

### Next Steps – Project Setup

- Create the project README.
- Select and document a dataset.
- Perform exploratory data analysis.
- Build a baseline machine learning model.

## 10 September 2026 – Dataset Exploration

### Work Completed – Dataset Exploration

- Added the Loan Approval dataset to the project.
- Created an exploratory data analysis script.
- Loaded the dataset using Pandas.
- Checked dataset dimensions and column names.
- Examined data types.
- Identified missing values.
- Examined the target variable distribution.
- Analyzed Gender subgroup distribution.
- Analyzed Education subgroup distribution.

### Key Findings

- The dataset contains 614 records and 13 columns.
- The target variable is `Loan_Status`.
- There are 422 approved loan records and 192 rejected loan records.
- Gender and Education are available for subgroup fairness evaluation.
- The Gender attribute contains missing values.
- Several features contain missing values, including Credit_History, LoanAmount and Self_Employed.
- The Gender groups are not equally represented, which may affect the reliability of subgroup fairness metrics.

### Next Steps – Dataset Exploration

- Implement data validation.
- Define normal, edge and incomplete input cases.
- Handle missing values for model training.
- Prepare a baseline machine learning model.

## 02 October 2026 – Data Validation and Test Cases

### Work Completed – Data Validation and Test Cases

- Implemented the initial dataset validation module.
- Verified that all required dataset columns are present.
- Checked for duplicate records.
- Identified and reported missing values.
- Validated the `Loan_Status` target values.
- Created normal test cases.
- Created edge test cases.
- Created incomplete test cases.
- Documented testing assumptions and acceptance criteria.

### Validation Results

- Dataset loaded successfully.
- All required columns were present.
- No duplicate rows were detected.
- Missing values were identified and reported.
- No invalid `Loan_Status` values were detected.

### Governance Considerations

- Missing demographic information should remain visible during evaluation.
- Edge cases should be flagged for additional review.
- Incomplete cases should not be treated as fully evaluated cases.
- Small subgroup sizes may affect the reliability of fairness metrics.

### Next Steps – Baseline Model

- Commit the validation and testing work to GitHub.
- Prepare the baseline machine learning model.
- Evaluate baseline model performance before adding fairness and explainability components.

## 02 October 2026 – Baseline Machine Learning Model

### Work Completed – Baseline Model

- Implemented the preprocessing pipeline for the loan dataset.
- Split the dataset into training and testing sets using stratified sampling.
- Handled missing numerical values using median imputation.
- Handled missing categorical values using most-frequent imputation.
- Applied one-hot encoding to categorical features.
- Applied standard scaling to numerical features.
- Excluded `Gender` and `Education` from model inputs so they can be retained for later fairness evaluation.
- Trained a Logistic Regression baseline model.
- Saved the trained model and preprocessing pipeline.
- Evaluated baseline model performance.

### Dataset Split

- Total rows: 614
- Training rows: 491
- Testing rows: 123

### Baseline Results

- Accuracy: 86.18%
- Precision: 84.00%
- Recall: 98.82%
- F1 Score: 90.81%

### Confusion Matrix

- True Negative: 22
- False Positive: 16
- False Negative: 1
- True Positive: 84

### GenAI Safety Governance Significance

The baseline model establishes a performance reference point before fairness, explainability and governance checks are applied.

The `Gender` and `Education` attributes are retained separately for subsequent subgroup fairness analysis.

### Next Steps – Fairness Evaluation

- Evaluate fairness across demographic subgroups.
- Calculate subgroup performance and selection metrics.
- Identify potential fairness gaps requiring governance review.

## 02 October 2026 – Fairness Evaluation

### Work Completed – Fairness Evaluation

- Implemented fairness evaluation using Fairlearn.
- Evaluated model behavior across Gender subgroups.
- Evaluated model behavior across Education subgroups.
- Calculated subgroup accuracy, recall and selection rate.
- Calculated demographic parity difference.
- Calculated equalized odds difference.
- Stored fairness results as JSON governance evidence.

### Gender Fairness Results

| Group | Accuracy | Recall | Selection Rate |
| --- | ---: | ---: | ---: |
| Female | 84.00% | 100.00% | 72.00% |
| Male | 87.50% | 98.57% | 83.33% |

- Demographic Parity Difference: 0.1133
- Equalized Odds Difference: 0.0594

### Education Fairness Results

| Group | Accuracy | Recall | Selection Rate |
| --- | ---: | ---: | ---: |
| Graduate | 86.00% | 98.59% | 83.00% |
| Not Graduate | 86.96% | 100.00% | 73.91% |

- Demographic Parity Difference: 0.0909
- Equalized Odds Difference: 0.1149

### Fairness Governance Considerations

- Fairness metrics are treated as evidence rather than automatic proof of unfairness.
- Differences in selection rates and error-related metrics require contextual review.
- Subgroup size and missing demographic information must be considered when interpreting fairness results.
- Gender and Education were not used as model inputs but were retained for subgroup evaluation.

### Next Steps – Explainability and Governance

- Add an explainability component using SHAP.
- Identify important model features.
- Connect explanations with governance evidence.

## 02 October 2026 – Explainable AI with SHAP

### Governance Engine Work Completed

- Implemented SHAP-based explainability for the baseline Logistic Regression model.
- Generated SHAP values for the test dataset.
- Calculated mean absolute SHAP values for model features.
- Ranked features according to their average contribution magnitude.
- Saved explainability results as JSON governance evidence.

### Top Features by Mean Absolute SHAP Value

| Feature | Mean Absolute SHAP |
| --- | ---: |
| Credit_History | 1.0261 |
| Property_Area_Semiurban | 0.2243 |
| Property_Area_Rural | 0.1400 |
| Married_Yes | 0.1124 |
| Married_No | 0.1118 |
| Dependents_1 | 0.1007 |
| CoapplicantIncome | 0.0803 |
| Dependents_2 | 0.0710 |
| Property_Area_Urban | 0.0654 |
| Self_Employed_No | 0.0248 |

### Explainability Governance Significance

SHAP provides evidence about which model features have the greatest influence on predictions.

Feature importance magnitude does not by itself establish causality or fairness. Explainability results should therefore be interpreted together with performance and subgroup fairness evidence.

### Next Steps – Governance Decision Engine

- Add controlled Generative-AI safety testing.
- Define prompt-risk categories and safety checks.
- Record GenAI test results as governance evidence.

## 02 October 2026 – Controlled Generative-AI Safety Testing

### Work Completed – Controlled Generative-AI Safety Testing

- Defined controlled GenAI safety test cases.
- Added normal, fairness, high-risk, discrimination, privacy, incomplete and ambiguous scenarios.
- Implemented a rule-based GenAI safety evaluator.
- Classified requests into SAFE, BLOCK and REVIEW outcomes.
- Generated governance evidence for each test case.
- Verified expected and actual safety outcomes.

### Safety Evaluation Results

- Total cases: 8
- Passed cases: 8
- Failed cases: 0
- Predefined test-case match rate: 100%

### Governance Outcomes

| Outcome | Cases |
| --- | ---: |
| SAFE | 3 |
| BLOCK | 3 |
| REVIEW | 2 |

### Governance Significance

The safety evaluator demonstrates controlled handling of different GenAI risk categories.

High-risk requests are blocked, while incomplete or ambiguous requests are routed for review rather than being automatically accepted.

The 100% result represents agreement with the predefined test expectations and does not establish that a real-world GenAI system is completely safe.

### Next Steps

- Build the governance decision engine.
- Combine model performance, fairness, explainability and GenAI safety evidence.
- Generate an overall governance status and recommended review actions.

## 02 October 2026 – Governance Decision Engine

### Work Completed

- Implemented a transparent rule-based governance decision engine.
- Combined baseline model performance evidence.
- Combined Gender fairness evidence.
- Combined Education fairness evidence.
- Included SHAP explainability evidence.
- Included GenAI safety evaluation evidence.
- Generated an overall governance status.
- Generated governance actions for conditions requiring additional review.
- Saved the complete governance decision as JSON evidence.

### Governance Decision

- Overall status: REVIEW

### Reason for Review

The fairness evaluation identified subgroup metric differences that crossed the configured review conditions.

The governance engine therefore routes the model for additional human review rather than automatically treating the model as deployment-ready.

### Governance Evidence

The decision incorporates:

- Model performance metrics
- Demographic parity difference
- Equalized odds difference
- Subgroup performance
- SHAP feature importance
- GenAI safety test results
- Explicit governance actions

### Governance Principle

The governance engine is designed to support human oversight. A rule-based status provides traceable evidence for review rather than replacing human judgment.

### Next Steps – Governance Dashboard

- Build the Streamlit governance dashboard.
- Display performance, fairness, explainability and GenAI safety evidence.
- Display the governance status and review actions.
- Add visualizations for subgroup comparisons and feature importance.
