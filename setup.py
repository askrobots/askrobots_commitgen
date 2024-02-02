from setuptools import setup, find_packages

setup(
    name="AskRobotsCommitGen",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["openai", "python-dotenv"],  # Add other dependencies as needed
)
