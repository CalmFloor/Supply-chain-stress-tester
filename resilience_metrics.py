import pandas as pd
import numpy as np
# Load your simulation results
stress = pd.read_csv('stress_results.csv')
resilient = pd.read_csv('resilient_results.csv')

def calculate_resilience(df, initial_stock=50, daily_demand=5):
    stock = initial_stock
    tts = 0
    ttr = len(df) # Default to max if it never recovers
    survived = True
    
    for i, row in enumerate(df.itertuples()):
        # 1. Lead Time Logic: If delay is > 5 days, assume the shipment is 'stuck'
        # and doesn't arrive to replenish stock today.
        if row.simulated_lead_time > 5:
            replenishment = 0
        else:
            replenishment = daily_demand # Normal replenishment
            
        # 2. Update Stock
        stock = (stock + replenishment) - daily_demand
        
        # 3. Check TTS (When do we run out?)
        if stock <= 0 and survived:
            tts = row.day
            survived = False
            
        # 4. Check TTR (When do we get back to initial levels?)
        if not survived and stock >= initial_stock:
            ttr = row.day - tts # Time from failure to recovery
            break
            
    return tts, ttr

# Compare the two
tts_s, ttr_s = calculate_resilience(stress)
tts_r, ttr_r = calculate_resilience(resilient)

print(f"--- RESILIENCE METRICS ---")
print(f"STRESSED: TTS = {tts_s} days, TTR = {ttr_s} days")
print(f"RESILIENT: TTS = {tts_r if tts_r > 0 else 'Infinite'} days, TTR = {ttr_r} days")

# Load your stress test results
df_stress = pd.read_csv('stress_results.csv')

# Step 1: Define your Cost per Day of Delay (e.g., $5,000 per day in lost sales/fees)
cost_per_day = 5000 

# Step 2: Calculate the financial loss for every simulated day
# This creates a distribution of potential losses
losses = df_stress['simulated_lead_time'] * cost_per_day

# Step 3: Calculate VaR at 95% Confidence
# This finds the "cutoff" where 95% of losses are below this number
var_95 = np.percentile(losses, 95)

print(f"95% Value at Risk (VaR): ${var_95:,.2f}")
print(f"Meaning: In a Black Swan event, we are 95% sure our loss won't exceed ${var_95:,.2f}")
