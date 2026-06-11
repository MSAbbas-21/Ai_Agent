Chatbot Agent
A simple Python chatbot powered by the OpenAI API. This project demonstrates how to build an interactive command‑line chatbot that responds to user input using GPT models.

🚀 Features
Interactive chatbot loop (bye to exit).
Uses OpenAI’s ChatCompletion API.
Customizable system prompt for chatbot personality.
Reads API key securely from environment variables.

📦 Requirements
Python 3.9+ (tested with Python 3.13)
OpenAI Python library (pip install openai)

🔑 Setup
1. Install dependencies  [pip install openai]
2. Set your API key
On Windows PowerShell:  [setx OPENAI_API_KEY "sk-proj-xxxxxxxxxxxxxxxxxxxxxxxx"]
3. Verify the key
Run:  import os
print(os.getenv("OPENAI_API_KEY"))

▶️ Usage
Run the chatbot:python main.py

📂 Project Structure
chatbott/
│
├── main.py        # Chatbot code
├── README.md      # Project documentation
