import os
from pathlib import Path
import logging

# keep a log of basic info
logging.basicConfig(Level=logging.INFO, format="[%(asctime%)s]: %(message)s:")

project_name = "textSummarizer"

# list of file I wanna create
# whenever you are working on big project/enterprize level projects these are the core components which are required
list_of_files = [
    # .gitkeep is a hidden file
    ".github/workflows/.gitkeep", # thiss will be used during deployment, ci/cd deployment. this will contain ci/cd related deployment file
    # so whenever I do a commit it'll pick it up and deploy it on the cloud
    f"src/{project_name}/__init__.py", # to do some importing to local
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/utils/__init__.py", 
    f"src/{project_name}/utils/common.py", 
    f"src/{project_name}/logging/__init__.py", 
    f"src/{project_name}/config/__init__.py", 
    f"src/{project_name}/config/configuration.py", 
    f"src/{project_name}/pipeline/__init__.py", # it'll contact over training and prediction pipeline
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py", 
    "config/config.yaml", 
    "params.yaml", # will keep all model related params here
    "app.py",
    "main.py",
    "Dockerfile", # will create a docker image
    "requirements.txt", # will create a docker image
    "setup.py",
    "research/trials.ipynb"
    
]