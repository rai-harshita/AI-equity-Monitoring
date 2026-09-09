# Development Log

## 10 September 2026

### Work Completed

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
