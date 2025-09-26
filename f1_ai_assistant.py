import os
from dotenv import load_dotenv
import google.generativeai as genai
import fastf1 as ff
keystatus = False
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    print("Error: GOOGLE_API_KEY not found in .env file. Please create one.")
    exit()
else:
    keystatus = True
    genai.configure(api_key=GOOGLE_API_KEY)


