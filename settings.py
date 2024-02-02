import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# OpenAI Model to be used for generating commit messages
OPENAI_MODEL = "gpt-4"  # Replace with the correct model name if different

# The maximum length of the commit message
MAX_COMMIT_MESSAGE_LENGTH = 200

# Any other global settings can be added here
# For example, the language for the commit messages, if you plan to support multiple languages
DEFAULT_LANGUAGE = 'en'
