from setuptools import find_packages, setup

# Read the contents of the README file for the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Package metadata
__version__ = "0.0.0"
REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "Ahmed Osman"
SRC_REPO = "textSummarizer" # It will be the main local package 
AUTHOR_EMAIL = "engineer.ahmedfarouk@gmail.com"


# Setup function to specify package details
setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[],
)