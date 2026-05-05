import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data
baseline = pd.read_csv('baseline_results.csv')
stress = pd.read_csv('stress_results.csv')

# 2. Setup the plot
plt.figure(figsize=(12, 6))

# Plot Baseline
plt.plot(baseline['day'], baseline['simulated_lead_time'], 
         label='Normal Operations', color='blue', linestyle='--', alpha=0.6)

# Plot Stress (Overlaying it on the same days)
plt.plot(stress['day'], stress['simulated_lead_time'], 
         label='Black Swan: Megafire', color='red', linewidth=2)

# 3. Add formatting
plt.title('Supply Chain Lead Time: Normal vs. Black Swan Disruption', fontsize=14)
plt.xlabel('Day of Simulation', fontsize=12)
plt.ylabel('Lead Time (Days)', fontsize=12)
plt.axhline(y=baseline['simulated_lead_time'].mean(), color='blue', alpha=0.3, label='Avg Normal')
plt.grid(axis='y', alpha=0.3)
plt.legend()

# Save the visual
plt.savefig('impact_chart.png')
print("Chart saved as 'impact_chart.png' - Open it in VS Code to see the results!")
plt.show()