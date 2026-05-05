import pandas as pd
import numpy as np

# Load the dataset
# Note: encoding='ISO-8859-1' is often required for this specific dataset
df = pd.read_csv('DataCoSmartSupplyChainData.csv', encoding='ISO-8859-1')

def run_normal_simulation(days=30):
    # Use the exact column names from your CSV
    real_days_col = 'Days for shipping (real)'
    sched_days_col = 'Days for shipment (scheduled)'
    
    # Calculate baseline stats
    # We use the 'real' shipping days to find our operational mean and sigma
    lead_time_mu = df[real_days_col].mean()
    lead_time_sigma = df[real_days_col].std()
    
    print(f"Baseline Calculated: Mean={lead_time_mu:.2f}, StdDev={lead_time_sigma:.2f}")
    
    results = []
    for day in range(days):
        # Generate a random lead time based on the Normal Distribution of the data
        simulated_delay = np.random.normal(lead_time_mu, lead_time_sigma)
        
        results.append({
            "day": day + 1,
            "simulated_lead_time": max(0, simulated_delay), # Lead time can't be negative
            "status": "Normal"
        })
        
    return pd.DataFrame(results)

# Run and save
baseline_df = run_normal_simulation(30)
baseline_df.to_csv('baseline_results.csv', index=False)
print("Normal Simulation Complete. Baseline saved to 'baseline_results.csv'")