import os
from dotenv import load_dotenv
import google.generativeai as genai
import fastf1 as ff

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    print("Error: GOOGLE_API_KEY not found in .env file. Please create one.")
    exit()
else:
    print("API key found")

