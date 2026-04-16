from setuptools import find_packages,setup
from typing import List

def get_requiremnets()->list[str]:
    """
    This function will return all the requiremnets
    """
    try:
        requirement_lst = []
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileExistsError:
        print("File Not found")

    return requirement_lst

setup(
    name = "Network_Security",
    version = "3.01.12",
    author = "Jhon Dhue",
    author_email="example@gmail.com",
    packages=find_packages(),
    install_requires=get_requiremnets()
    )



