import os
import sys
from dotenv import load_dotenv
from google import genai

if len(sys.argv) <= 1 :
    print("Error 1: No prompt specified")
    sys.exit(1)

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents= sys.argv
)
print(response.text)

usage = response.usage_metadata

print(f"Prompt tokens: {usage.prompt_token_count}")
print(f"Response tokens: {usage.candidates_token_count}")