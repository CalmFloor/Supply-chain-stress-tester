import pandas as pd
import numpy as np
import json

# 1. Load everything: Data, Disaster, and the Strategy
df = pd.read_csv('DataCoSmartSupplyChainData.csv', encoding='ISO-8859-1')

with open('black_swan_profile.json', 'r') as f:
    disaster = json.load(f)

with open('mitigation_strategy.json', 'r') as f:
    strategy = json.load(f)

def run_resilient_simulation():
    real_days_col = 'Days for shipping (real)'
    lead_time_mu = df[real_days_col].mean()
    lead_time_sigma = df[real_days_col].std()
    
    # 2. Calculate the "Defended" Sigma
    # We take the original disaster multiplier but reduce its impact by the strategy's factor
    # Formula: Baseline Sigma * (Disaster Multiplier * (1 - Reduction Factor))
    impact_reduction = (1 - strategy['risk_reduction_factor'])
    mitigated_sigma = lead_time_sigma * (disaster['delay_multiplier'] * impact_reduction)
    
    duration = disaster['event_duration_days']
    
    print(f"--- RUNNING DEFENSE: {strategy['strategy_name']} ---")
    
    results = []
    for day in range(duration):
        # Generate the dampened lead times
        simulated_delay = np.random.normal(lead_time_mu, mitigated_sigma)
        
        results.append({
            "day": day + 1,
            "simulated_lead_time": max(0, simulated_delay),
            "status": "MITIGATED",
            "strategy": strategy['strategy_name']
        })
        
    return pd.DataFrame(results)

# 3. Save the results
resilient_df = run_resilient_simulation()
resilient_df.to_csv('resilient_results.csv', index=False)
print("\nResilient Simulation Complete. Results saved to 'resilient_results.csv'")