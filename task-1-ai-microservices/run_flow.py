import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

LANGFLOW_SERVER_URL = os.getenv("LANGFLOW_SERVER_URL", "http://127.0.0.1:7860")
LANGFLOW_API_KEY = os.getenv("LANGFLOW_API_KEY")
FLOW_ID = os.getenv("LANGFLOW_FLOW_ID")

def run_flow(input_text: str):
    url = f"{LANGFLOW_SERVER_URL}/api/v1/run/{FLOW_ID}?stream=false"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": LANGFLOW_API_KEY
    }
    payload = {
        "input_value": input_text,
        "input_type": "chat",
        "output_type": "chat",
        "tweaks": {}
    }
    resp = requests.post(url, headers=headers, json=payload)
    resp.raise_for_status()
    return resp.json()

if __name__ == "__main__":
    input_text = input("Enter text for the flow: ")
    output = run_flow(input_text)
    print(json.dumps(output, indent=2))
