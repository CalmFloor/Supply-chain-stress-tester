import pandas as pd

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