from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements
    """
    requirements=[]
    with open(file_path) as file_obj:
        try:
            requirements = [
                req.strip() for req in file_obj
                if req.strip() and req.strip() != '-e .'
            ]
            
        except FileNotFoundError:
            print("requirements.txt file not found")
        
    return requirements

setup(
    name="Network Security",
    version="0.0.1",
    author="Apurva",
    author_mail="apurva.kondekar6@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('D:/NETWORK SECURITY/requirements.txt')
    )