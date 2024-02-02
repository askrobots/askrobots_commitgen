# AskRobotsCommitGen

## Overview
AskRobotsCommitGen is an AI-powered tool designed to generate meaningful git commit messages. It leverages OpenAI's GPT model to analyze your git diffs and suggest concise, relevant commit messages. The tool can now automatically commit changes with the generated message.

Additionally, it includes a command to modify existing files with AI, running like `ar-ai-modify notes.txt "Make a list of the most common git commands used by django devs"`. This offers an effective method to edit files for Django developers streamlining their workflow with common git commands.

## Features
- AI-powered commit message generation.
- Easy integration with existing git workflows.
- Option to automatically commit changes with the AI-generated message.
- AI-powered file modification with specific instructions.
- Customizable message formats.

## Prerequisites
- Python 3.7 or higher
- Git

## Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/askrobots_commitgen.git
cd askrobots_commitgen
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```


## Configuration
Set up your OpenAI API key in an environment variable:
```bash
export OPENAI_API_KEY='your-api-key'
```

## Usage
Run the script in your git repository:

To automatically commit changes with the AI-generated message:
```bash
python main.py
```

To only display the generated commit message without committing:
```bash
python main.py --show-only
```

To modify a file with AI, run the following command:
```bash
ar-ai-modify notes.txt "Make a list of the most common git commands used by django devs"
```

## Contributing
Contributions to AskRobotsCommitGen are welcome! Please read our contributing guidelines for details on how to contribute.

## License
AskRobotsCommitGen is open-sourced software licensed under the [MIT license](LICENSE).

## Contact
For questions or feedback, please reach out to [dan@quellhorst.com](mailto:dan@quellhorst.com).

## Acknowledgments
- This project is inspired by [aicommit](https://github.com/Nneji123/aicommit).
- Thanks to OpenAI for providing the GPT API.