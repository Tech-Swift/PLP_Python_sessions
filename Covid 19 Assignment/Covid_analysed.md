
# 📊 COVID-19 Data Analysis: Summary of Findings

## ✅ Key Insights

1. **The United States had the highest number of total cases and deaths** among the selected countries (Kenya, India, United States), with a steady rise over time.
2. **India experienced the most dramatic spikes** in daily new cases, notably during the second wave.
3. **Vaccination efforts varied significantly**: The United States showed the fastest vaccine rollout, while Kenya had the slowest uptake.
4. **Death rates remained below 5%** across all countries, though this varied slightly depending on surges and healthcare capacity.
5. **Total vaccinations sometimes exceeded population counts**, indicating doses per person (e.g., 2-dose regimens), requiring adjustment to avoid overestimation.

## ⚠️ Notable Anomalies and Patterns

- In some countries, `total_vaccinations` exceeded the `population`, likely due to booster shots or multiple-dose vaccines. This required capping values when computing vaccination percentages.
- Correlation heatmap showed a **strong positive correlation between total cases and total deaths**, validating expected relationships in the pandemic data.
- Despite lower case counts, **Kenya had periods where its death rate appeared relatively higher**, possibly due to testing limitations or healthcare access.
