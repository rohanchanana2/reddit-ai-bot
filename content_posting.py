import praw
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Authenticate with Reddit and return the Reddit client instance.
def authenticate_reddit(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD, REDDIT_USER_AGENT):
    try:
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            username=REDDIT_USERNAME,
            password=REDDIT_PASSWORD,
            user_agent=REDDIT_USER_AGENT
        )
        logging.info("Authenticated with Reddit successfully.")
        return reddit
    except Exception as e:
        logging.error(f"Error authenticating with Reddit: {e}")
        return None

# Post content to a specific subreddit.
def post_to_reddit(reddit, content, subreddit_name, title):
    try:
        subreddit = reddit.subreddit(subreddit_name)
        submission = subreddit.submit(title, selftext=content)
        logging.info(f"Posted to Reddit with title '{title}': {submission.url}")
    except Exception as e:
        logging.error(f"Error posting to Reddit: {e}")
