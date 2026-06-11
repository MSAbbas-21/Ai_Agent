import os
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

import os
import openai

# Test if the environment variable is available
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4o-mini" if available
            messages=[
                {"role": "system", "content": "You are a clever chatbot that helps people learn."},
                {"role": "user", "content": user_input}
            ]
        )

        print("Chatbot:", response.choices[0].message["content"])

if __name__ == "__main__":
    chatbot()
