from openai import AzureOpenAI
import os
import configparser
import re

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(PROJECT_ROOT, "config.properties")

# Read credentials from config file
config = configparser.RawConfigParser()
config.read(config_path)

AZURE_OPENAI_API_KEY = config['env']['AZURE_OPENAI_API_KEY']
AZURE_OPENAI_ENDPOINT = config['env']['AZURE_OPENAI_ENDPOINT']
AZURE_OPENAI_DEPLOYMENT = config['env']['AZURE_OPENAI_DEPLOYMENT']

# configure Azure OpenAI service client
client = AzureOpenAI(
  azure_endpoint =AZURE_OPENAI_ENDPOINT,
  api_key=AZURE_OPENAI_API_KEY,
  api_version = "2023-10-01-preview"
  )


def get_aircraft_maintenance_response(aircraft_id):
  # Validate aircraft id format
  if not re.match(r"^AC-\d{3}$", aircraft_id):
    return "Invalid format. Please enter the aircraft id in the format AC-###."

  # Define the structured prompt with context
  prompt = (
    f"You are an AI assistant specialized in aircraft maintenance. "
    f"For this simulation, you will generate a response based on the aircraft ID provided, even if the details are fictitious. "
    f"Please follow the structured format and ensure the response is coherent and relevant.\n\n"
    f"Aircraft ID: {aircraft_id}\n"
    "Provide a summary of the aircraft's current status, potential anomalies, and any additional maintenance needs or recommendations.\n\n"
    "Structure your response as follows:\n"
    "1. Aircraft Status Summary: Brief overview of the aircraft's operational state.\n"
    "2. Potential Anomalies: List of detected anomalies with details.\n"
    "3. Related Needs/Recommendations: Additional maintenance needs or recommendations based on the status and detected anomalies."
  )

  messages = [{"role": "user", "content": prompt}]

  # Get the completion from the LLM
  completion = client.chat.completions.create(model=AZURE_OPENAI_DEPLOYMENT, messages=messages, max_tokens=600,
                                              temperature=0.1)

  # Return the response content
  return completion.choices[0].message.content


if __name__ == "__main__":
  print('Welcome to your AIrcraft Maintenance Assistance')
  aircraft_id = input("Please enter the aircraft id (format: AC-###): ")
  response = get_aircraft_maintenance_response(aircraft_id)
  print(response)