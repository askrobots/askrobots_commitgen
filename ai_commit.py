from settings import OPENAI_API_KEY, OPENAI_MODEL, MAX_COMMIT_MESSAGE_LENGTH
import openai

def generate_commit_message(diff: str) -> str:
    try:
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model=OPENAI_MODEL,
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": f"Generate a commit message for the following diff:\n{diff}"}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error generating commit message: {e}")
        return ""
