def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"].strip()
    except openai.error.RateLimitError:
        return "Error: You’ve exceeded your quota. Please check your OpenAI account."
    except Exception as e:
        return f"Error: {str(e)}"
