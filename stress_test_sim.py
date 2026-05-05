import pandas as pd
import numpy as np
import json

# 1. Load your baseline data and the AI's disaster profile
df = pd.read_csv('DataCoSmartSupplyChainData.csv', encoding='ISO-8859-1')

with open('black_swan_profile.json', 'r') as f:
    disaster = json.load(f)

def run_stress_simulation():
    # Get baseline stats from the original data
    real_days_col = 'Days for shipping (real)'
    lead_time_mu = df[real_days_col].mean()
    lead_time_sigma = df[real_days_col].std()
    
    # 2. Apply the AI's "Mutators"
    # We multiply the standard deviation by the AI's multiplier to simulate chaos
    stressed_sigma = lead_time_sigma * disaster['delay_multiplier']
    duration = disaster['event_duration_days']
    
    print(f"--- STRESS TEST STARTING: {disaster['scenario_name']} ---")
    print(f"Injecting {disaster['delay_multiplier']}x variance for {duration} days...")

    results = []
    for day in range(duration):
        # Generate much more volatile delays
        simulated_delay = np.random.normal(lead_time_mu, stressed_sigma)
        
        results.append({
            "day": day + 1,
            "simulated_lead_time": max(0, simulated_delay),
            "status": "STRESSED",
            "scenario": disaster['scenario_name']
        })
        
    return pd.DataFrame(results)

# 3. Run and save the "After" picture
stress_df = run_stress_simulation()
stress_df.to_csv('stress_results.csv', index=False)
print("\nStress Simulation Complete. Results saved to 'stress_results.csv'")