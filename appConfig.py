from dotenv import load_dotenv
import os
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
FRONTEND_URL = os.getenv("FRONTEND_URL")
ANALYTICS_API_KEY = os.getenv("ANALYTICS_API_KEY")

