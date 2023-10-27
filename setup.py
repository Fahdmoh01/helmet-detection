from setuptools import find_packages, setup

AUTHOR_USERNAME = "Fahdmoh01"
REPO_NAME = "hatespeech"

setup(
    name="hatespeech",
    version="0.0.1",
    author="Fahd Mohammed",
    author_email="fahdmoh.1@gmail.com",
    packages=find_packages(where="src"),
    install_requires=[],
    description="A small python package for NLP app",
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
)
