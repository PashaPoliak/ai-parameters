import os
import requests
from task.constants import API_KEY, DIAL_ENDPOINT

def get_available_models():
    """
    Get available models from the DIAL API endpoint.
    Requires a valid API key in the DIAL_API_KEY environment variable.
    """
    if not API_KEY or API_KEY == 'your_api_key_here':
        print("Error: Please set the DIAL_API_KEY environment variable with a valid API key.")
        print("Example: set DIAL_API_KEY=your_actual_api_key (on Windows)")
        return None
    
    url = f"{DIAL_ENDPOINT}/openai/models"
    headers = {
        "api-key": API_KEY,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            models_data = response.json()
            print("Available models:")
            for model in models_data.get("data", []):
                print(f"- {model.get('id', 'N/A')}")
            return models_data
        else:
            print(f"Error: HTTP {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None

if __name__ == "__main__":
    print(f"Using API endpoint: {DIAL_ENDPOINT}")
    print("Attempting to get available models...")
    models = get_available_models()
