import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s: %(levelname)s]: %(message)s"
)

while True:
    project_name = input("Enter the Project Name: ")
    if project_name != "":
        break

logging.info(f"Creating project by name:{project_name}")


list_of_files = [
    ".github/workflows/.gitkeep/",
    f"flowcharts/"
    f"src/{project_name}/__init__.py",  # we need this to be able to import the package
    f"src/{project_name}/components/__init__.py",  # we need this to be able to import the package
    f"src/{project_name}/utils/__init__.py",  # we need this to be able to import the package
    f"src/{project_name}/utils/common.py",  # we need this to be able to import the package
    f"src/{project_name}/logging//__init__.py",  # we need this to be able to import the package
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",  # we need this to be able to import the package
    f"src/{project_name}/entity/__init__.py",  # we need this to be able to import the package
    f"src/{project_name}/constants/__init__.py",  # we need this to be able to import the package
    f"src/{project_name}/ml/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"File already exists: {filepath}")
