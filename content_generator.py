from groq import Groq
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_user_prompt(client):
    logging.info("Starting to generate a unique user prompt.")

    prompt = "Generate a unique and interesting topic for a Reddit post related to technology or society or any other trend. Output should be of max 10 words without using quotation mark and contain only the topic itself, no extra text, explanation."

    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-70b-8192",
    )

    user_prompt = chat_completion.choices[0].message.content.strip()
    logging.info(f"Generated user prompt: {user_prompt}")

    try:
        with open('topic_history.json', 'r') as file:
            history = json.load(file)
            logging.info("Loaded topic history successfully.")
    except FileNotFoundError:
        history = []
        logging.warning("topic_history.json not found, creating a new history.")

    while user_prompt in history:
        logging.info(f"'{user_prompt}' has already been used. Generating a new topic...")
        
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-70b-8192",
        )
        
        user_prompt = chat_completion.choices[0].message.content.strip()
        logging.info(f"Generated new unique user prompt: {user_prompt}")

    history.append(user_prompt)
    with open('topic_history.json', 'w') as file:
        json.dump(history, file)
    logging.info(f"Added '{user_prompt}' to topic history.")

    return user_prompt

def generate_content_with_groq(client, prompt):
    logging.info(f"Starting content generation for the topic: {prompt}")

    title_prompt = (
        f"Generate a short title for Reddit post about: {prompt}. Just the title strictly, also don't use quotes for title."
    )

    chat_completion_1 = client.chat.completions.create(
        messages=[{"role": "user", "content": title_prompt}],
        model="llama3-70b-8192",
    )

    title = chat_completion_1.choices[0].message.content.strip()
    logging.info(f"Generated title: {title}")

    content_prompt = (
        f"Generate creative, interesting and exciting content for a Reddit post about: {prompt} and which has title: {title}. Output should just have the content strictly, no extra comments, no title, also don't use quotes for content generated."
    )

    chat_completion_2 = client.chat.completions.create(
        messages=[{"role": "user", "content": content_prompt}],
        model="llama3-70b-8192",
    )

    content = chat_completion_2.choices[0].message.content.strip()
    logging.info(f"Generated content successfully.")

    return title, content
