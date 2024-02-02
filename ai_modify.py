import sys
from settings import OPENAI_API_KEY, OPENAI_MODEL
import openai

def modify_file(file_path: str, change_description: str) -> None:
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()

        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Modify the following file based on this description: '{change_description}'.\n\nFile content:\n{file_contents}\n\nModified file:"}
            ]
        )
        modified_contents = response['choices'][0]['message']['content'].strip()

        with open(file_path, 'w') as file:
            file.write(modified_contents)

        print(f"File '{file_path}' modified based on description: '{change_description}'")
    except Exception as e:
        print(f"Error modifying file: {e}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python ai_modify.py <file_path> <change_description>")
        return

    file_path = sys.argv[1]
    change_description = sys.argv[2]

    modify_file(file_path, change_description)

if __name__ == "__main__":
    main()
