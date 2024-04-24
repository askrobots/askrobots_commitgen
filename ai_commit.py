from settings import OPENAI_API_KEY, OPENAI_MODEL, MAX_COMMIT_MESSAGE_LENGTH
from openai import OpenAI
import os

# Assuming your API key is set in the environment or you set it somewhere in your settings
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

def generate_commit_message(diff: str) -> str:
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Generate a commit message for the following diff:\n{diff}"}
            ],
            model="gpt-3.5-turbo"  # Ensure you are using an appropriate model that you have access to
        )
        # Correctly accessing the first message content from the response
        if chat_completion and chat_completion.choices:
            return chat_completion.choices[0].message.content.strip()
        else:
            return "No valid response received from the API."
    except Exception as e:
        print(f"Error generating commit message: {e}")
        return ""

