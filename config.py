import os
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

logging.info(".env file loaded successfully.")

# Reddit API credentials
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
REDDIT_USERNAME = os.getenv('REDDIT_USERNAME')
REDDIT_PASSWORD = os.getenv('REDDIT_PASSWORD')
REDDIT_USER_AGENT = 'bot'  # App name

logging.info("Reddit credentials loaded from environment variables.")

# Groq API credentials
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

logging.info("Groq API credentials loaded from environment variables.")

if not all([REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD, GROQ_API_KEY]):
    logging.error("One or more required environment variables are missing!")
else:
    logging.info("All required environment variables are present.")
