import os
from pathlib import Path
import logging

# Configure logging to display the time and message format
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

# List of files and directories to be created for the project structure
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/components/_01_data_ingestion.py",
    f"src/{project_name}/components/_02_data_validation.py",
    f"src/{project_name}/components/_03_data_transformation.py",
    f"src/{project_name}/components/_04_model_trainer.py",
    f"src/{project_name}/components/_05_model_evaluation.py",

    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/prediction.py",
    f"src/{project_name}/pipeline/_01_data_ingestion.py",
    f"src/{project_name}/pipeline/_02_data_validation.py",
    f"src/{project_name}/pipeline/_03_data_transformation.py",
    f"src/{project_name}/pipeline/_04_model_trainer.py",
    f"src/{project_name}/pipeline/_05_model_evaluation.py",    

    "research/trials.ipynb",
    "research/_01_data_ingestion.ipynb",
    "research/_02_data_validation.ipynb",
    "research/_03_data_transformation.ipynb",
    "research/_04_model_trainer.ipynb",
    "research/_05_model_evaluation.ipynb",
    "research/Text_Summarization.ipynb",

    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",

    f"src/{project_name}/logging/__init__.py",

    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    
]


# Iterate over the list of files and create necessary directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create the directory if it does not exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    # Create an empty file if it does not exist or is of size zero
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exists")

