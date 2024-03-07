# chatbot_django.py

import openai
import sqlite3

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Connect to your SQLite database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Function to fetch user input from the database
def fetch_user_input():
    cursor.execute("SELECT input FROM user_inputs ORDER BY RANDOM() LIMIT 1")
    result = cursor.fetchone()
    return result[0] if result else None

# Function to interact with GPT-3 (IntelligentAI)
def chat_with_intelligentai(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Choose the appropriate GPT-3 engine
            prompt=prompt,
            max_tokens=150  # Adjust as needed
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error interacting with IntelligentAI: {e}")
        return "I'm sorry, but I couldn't process your request at the moment."

# Function to start the chat with IntelligentAI using database input
def intelligentai_chat_with_database():
    print("IntelligentAI: Hi! I'm IntelligentAI powered by GPT-3. How can I help you today? (Type 'bye' to exit)")
    while True:
        user_input = fetch_user_input()
        if not user_input:
            print("No more user inputs in the database. Exiting.")
            break

        print(f"You: {user_input}")
        if user_input.lower() == 'bye':
            print("IntelligentAI: Goodbye! Have a great day.")
            break

        prompt = f"You: {user_input}\nIntelligentAI:"
        response = chat_with_intelligentai(prompt)
        print(f"IntelligentAI: {response}")

# Close the database connection
conn.close()

# Start the IntelligentAI chat interaction with database input
if __name__ == "__main__":
    intelligentai_chat_with_database()
