import ollama
import json
import re  # New library to find patterns

def generate_black_swan_event(region="Southeast Asia"):
    prompt = f"""
    You are a Senior Supply Chain Risk Analyst. 
    Generate a high-impact 'Black Swan' disruption scenario for the supply chain hub in {region}.
    
    Return ONLY a JSON object. Do not include any introductory text.
    Keys required:
    - scenario_name
    - disruption_type
    - delay_multiplier (float 3.0 to 10.0)
    - capacity_loss (float 0.1 to 0.9)
    - event_duration_days (int 10 to 20)
    """
    
    response = ollama.chat(model='llama3', messages=[
        {'role': 'user', 'content': prompt}
    ])
    
    content = response['message']['content']
    
    try:
        # 1. Use regex to extract everything between the first { and last }
        json_match = re.search(r'\{.*\}', content, re.DOTALL)
        if json_match:
            clean_json = json_match.group(0)
            return json.loads(clean_json)
        else:
            raise ValueError("No JSON found in response")
            
    except Exception as e:
        print(f"Raw AI response was: {content}")
        raise e

# Run and save
disaster = generate_black_swan_event("Southeast Asia")
with open('black_swan_profile.json', 'w') as f:
    json.dump(disaster, f, indent=4)

print(f"Successfully generated: {disaster['scenario_name']}")