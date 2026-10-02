# Testing Strategy

## Purpose

The testing strategy verifies that the Responsible AI toolkit can identify normal, edge and incomplete cases before an AI model is evaluated for deployment.

## Normal Cases

Normal cases contain valid and sufficiently complete information.

### Normal Case Expected Result

PASS

The data can proceed to model evaluation.

## Edge Cases

Edge cases contain unusual values, low-confidence situations or subgroup conditions that require additional attention.

### Edge Case Expected Result

REVIEW

The system should flag these cases rather than silently treating them as ordinary cases.

## Incomplete Cases

Incomplete cases contain missing information that may prevent reliable evaluation.

### Incomplete Case Expected Result

INCOMPLETE

The system should prevent the evaluation from being considered complete until the missing information is addressed.

## Assumptions

- `Loan_Status` must contain only `Y` or `N`.
- Required dataset columns must be present.
- Missing demographic information should be explicitly identified.
- Missing values should not be silently removed without documentation.
- Small subgroup sizes may reduce the reliability of fairness metrics.
- Edge cases should be reviewed before deployment decisions.

## Acceptance Criteria

| Check | Acceptance Criterion |
| --- | --- |
| Required columns | All required columns are present |
| Target values | Only Y and N are accepted |
| Missing data | Missing values are identified |
| Duplicate records | Duplicate count is reported |
| Normal case | Classified as PASS |
| Edge case | Flagged for REVIEW |
| Incomplete case | Classified as INCOMPLETE |
| Evidence | Validation results are recorded |

## Governance Principle

A failed or incomplete validation should not be hidden by automatic preprocessing. The condition should remain visible as part of the governance evidence.
