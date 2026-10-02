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

### Work Completed

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

### Governance Significance

The baseline model establishes a performance reference point before fairness, explainability and governance checks are applied.

The `Gender` and `Education` attributes are retained separately for subsequent subgroup fairness analysis.

### Next Steps – Fairness Evaluation

- Evaluate fairness across demographic subgroups.
- Calculate subgroup performance and selection metrics.
- Identify potential fairness gaps requiring governance review.
