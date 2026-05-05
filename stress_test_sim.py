import pandas as pd
import numpy as np
import json

# 1. Load data
df = pd.read_csv('DataCoSmartSupplyChainData.csv', encoding='ISO-8859-1')

with open('black_swan_profile.json', 'r') as f:
    disaster = json.load(f)

def run_monte_carlo_stress(num_trials=1000):
    real_days_col = 'Days for shipping (real)'
    lead_time_mu = df[real_days_col].mean()
    lead_time_sigma = df[real_days_col].std()
    
    stressed_sigma = lead_time_sigma * disaster['delay_multiplier']
    duration = disaster['event_duration_days']
    
    print(f"--- RUNNING {num_trials} MONTE CARLO TRIALS ---")
    
    all_trial_results = []

    for trial in range(num_trials):
        trial_latencies = []
        for day in range(duration):
            simulated_delay = np.random.normal(lead_time_mu, stressed_sigma)
            trial_latencies.append(max(0, simulated_delay))
        
        # Capture the mean lead time for this specific trial
        all_trial_results.append({
            "trial_id": trial + 1,
            "avg_lead_time": np.mean(trial_latencies),
            "max_delay": np.max(trial_latencies),
            "scenario": disaster['scenario_name']
        })
        
    return pd.DataFrame(all_trial_results)

# 3. Run and Analyze
trials_df = run_monte_carlo_stress(num_trials=1000)

# Calculate the Global Mean across all trials
global_mean = trials_df['avg_lead_time'].mean()
print(f"\n--- FINAL RESULTS ---")
print(f"Across 1,000 simulations, the average lead time is: {global_mean:.2f} days")
print(f"The worst-case average seen in a single trial was: {trials_df['avg_lead_time'].max():.2f} days")

# Save summary
trials_df.to_csv('stress_mc_summary.csv', index=False)