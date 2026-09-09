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
