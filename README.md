# 🤖 Reddit AI Bot

This bot automates the process of generating unique content for Reddit and posting it to a specified subreddit at a scheduled time using Groq AI and Reddit's API.

## 🌟 Features

- **Reddit API Authentication:** Seamlessly integrates with Reddit's API for posting to subreddits.
- **Automated Topic and Content Generation:** Uses Groq AI to automatically generate relevant and engaging Reddit topics and content. No manual topic input needed.
- **Model Used:** The bot uses **Groq AI's llama3-70b-8192** model to generate high-quality, creative content.
- **Scheduled Posting:** Set the bot to post content at a specific time each day.
- **Logging and Error Handling:** Basic logging tracks post status and logs errors for troubleshooting.

## 🔄 How it Works

1. **Automatic Idea Generation:** The bot generates unique, creative topics, with no manual input. If a topic has been used before, it generates a new one.
  
2. **Content Generation:** Using the generated topic, the bot sends it to Groq's AI model to generate engaging and Reddit-optimized content.

3. **Reddit Posting:** The bot posts the generated content and title to the specified subreddit at the scheduled time, all fully automated.

4. **Logging and Monitoring:** The bot logs key activities like successful posts and errors, making it easy to track and resolve any issues.


## 🛠️ Setup Instructions

1. **Clone the repository**

   Clone the repository to your local machine using Git

3. **Install dependencies**

   pip install -r requirements.txt

3. **Create a .env file**

   In the root directory of the project, create a .env file and add the following :<br>
   REDDIT_CLIENT_ID=your_reddit_client_id<br>
   REDDIT_CLIENT_SECRET=your_reddit_client_secret<br>
   REDDIT_USERNAME=your_reddit_username<br>
   REDDIT_PASSWORD=your_reddit_password<br>
   REDDIT_USER_AGENT=bot<br>
   GROQ_API_KEY=your_groq_api_key

5. **Run the bot**

   Once the .env file is set up, run the bot with the following command :<br>
   python reddit_bot.py
