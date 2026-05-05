import pandas as pd

# 1. Load both files
baseline = pd.read_csv('baseline_results.csv')
stress = pd.read_csv('stress_results.csv')

# 2. Calculate KPIs
avg_base = baseline['simulated_lead_time'].mean()
avg_stress = stress['simulated_lead_time'].mean()

max_base = baseline['simulated_lead_time'].max()
max_stress = stress['simulated_lead_time'].max()

increase_pct = ((avg_stress - avg_base) / avg_base) * 100

# 3. Print the Summary
print("--- SUPPLY CHAIN IMPACT REPORT ---")
print(f"Scenario: {stress['scenario'].iloc[0]}")
print(f"Disruption Duration: {len(stress)} days")
print("-" * 35)
print(f"Average Lead Time (Normal): {avg_base:.2f} days")
print(f"Average Lead Time (Stress): {avg_stress:.2f} days")
print(f"Impact: {increase_pct:.1f}% increase in delays")
print("-" * 35)
print(f"Worst Case (Normal): {max_base:.2f} days")
print(f"Worst Case (Stress): {max_stress:.2f} days")