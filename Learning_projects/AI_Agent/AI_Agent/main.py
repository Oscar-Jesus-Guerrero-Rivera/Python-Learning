import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai

if len(sys.argv) <= 1:
    print("Error 1: No prompt specified")
    sys.exit(1)

user_prompt = sys.argv[1]

# acepta verbose con o sin guiones
if len(sys.argv) >= 3 and sys.argv[2].lstrip("-") == "verbose":
    verbose = True
else:
    verbose = False

if verbose:
    print(f"User Prompt: {user_prompt}")

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash-001")

response = model.generate_content(user_prompt)

print(response.text)

usage = response.usage_metadata

if verbose:
    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")
