# Dataset Documentation

## Dataset Purpose

This dataset will be used to develop and evaluate the machine learning component of the Responsible AI Equity Monitoring and Model Governance Toolkit.

The selected use case is loan approval prediction.

The machine learning model will predict whether a loan application is approved or rejected based on applicant-related attributes.

## Intended Target Variable

Loan_Status

Possible values:

- 1 → Loan Approved
- 0 → Loan Rejected

## Planned Features

The project may evaluate features such as:

- Gender
- Married
- Dependents
- Education
- Self_Employed
- ApplicantIncome
- CoapplicantIncome
- LoanAmount
- Loan_Amount_Term
- Credit_History
- Property_Area

## Fairness Evaluation Attributes

The initial fairness evaluation will focus on:

- Gender
- Education

These attributes will be used for subgroup analysis.

## Important Assumptions

This dataset is being used for educational and research purposes.

The loan approval use case is simulated for demonstrating Responsible AI governance concepts.

The model predictions must not be interpreted as real financial decisions.

## Planned Evaluation

The dataset will be used to evaluate:

- Model Accuracy
- Precision
- Recall
- F1 Score
- Subgroup Performance
- Selection Rate
- Demographic Parity Difference
- Equal Opportunity Difference

## Known Limitations

- Dataset quality may affect fairness results.
- Demographic attributes may not represent all real-world populations.
- Small subgroup sizes can produce unstable fairness estimates.
- The model is for educational demonstration only.

## Initial Data Exploration Findings

The dataset contains 614 records and 13 columns.

The target variable is `Loan_Status`, where:

- Y represents loan approval.
- N represents loan rejection.

### Subgroup Distribution

Gender:

- Male: 489 records
- Female: 112 records
- Missing: 13 records

Education:

- Graduate: 480 records
- Not Graduate: 134 records

### Missing Data

Missing values were identified in the following attributes:

- Gender: 13
- Married: 3
- Dependents: 15
- Self_Employed: 32
- LoanAmount: 22
- Loan_Amount_Term: 14
- Credit_History: 50

These missing values will be documented as a data quality consideration and will also be used when creating incomplete-case tests for the governance toolkit.
