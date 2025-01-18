import logging
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD, REDDIT_USER_AGENT, GROQ_API_KEY
from groq import Groq
import schedule
import time
from content_posting import post_to_reddit, authenticate_reddit
from content_generator import generate_content_with_groq, generate_user_prompt

# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Groq API client
client = Groq(api_key=GROQ_API_KEY)

# Authenticate with Reddit
reddit = authenticate_reddit(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD, REDDIT_USER_AGENT)

# Generate user prompt for content generation
user_prompt = generate_user_prompt(client)
subreddit_name = 'r/YOUR_SUBREDDIT_NAME'
post_time = '00:00'  # Enter the posting time (HH:MM format)

################### Uncomment below 2 lines to post manually ###################
# title, content = generate_content_with_groq(client, user_prompt)
# post_to_reddit(reddit, content, subreddit_name, title)


################### Comment all lines below to post manually ###################
def run_bot(user_prompt, subreddit_name):
    logging.info("Bot started running... Generating content.")
    title, content = generate_content_with_groq(client, user_prompt)
    logging.info(f"Generated content with title: {title}")
    post_to_reddit(reddit, content, subreddit_name, title)
    logging.info(f"Posted content to Reddit with title: {title}")

def schedule_posting(user_prompt, subreddit_name, post_time):
    logging.info(f"Scheduling bot to post at {post_time} every day.")
    schedule.every().day.at(post_time).do(run_bot, user_prompt=user_prompt, subreddit_name=subreddit_name)
    logging.info(f"Bot scheduling started. Posts will be made daily at {post_time}.")
    
    while True:
        schedule.run_pending()
        time.sleep(1)

schedule_posting(user_prompt, subreddit_name, post_time)
