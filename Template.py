import os
from pathlib import Path
import logging

# keep a log of basic info
# "But how does this work"
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

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

# in linus we use forward slash and in win we use backward slash
# so we'll have to get it in a suitable format with the help of "pathlib" before creating dir 
# >>> path = "something/someone"
# >>> Path(path)
# WindowsPath('something/someone')

for filepath in list_of_files:
    filepath = Path(filepath)
    #create file dir and then the files with os.split
    filedir, filename = os.path.split(filepath)

    # if you already have the folder, it wont be creating a new one.
    if filedir != "": ### "come back and get a better understanding of this logic"
        os.makedirs(filedir, exist_ok=True)
        # return what is happening to keep track or for debugging 
        logging.info(f"Creating directory:{filedir} for the file {filename}") 

        # if the filepath does not exist or it's size is zero
        # returns zero when there is nothing in the file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # it'll try to write it so if it doesnt exists itll make one
        with open(filepath, 'w') as f:
            pass # we just wanna create it and not do anything else in it.
            logging.info(f'Creating empty file: {filepath}')
        
    

    else:
        logging.info(f"{filename} already exists")

    
