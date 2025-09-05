"""

The setup.py is an essential part of packaging and dsitributing python projects. it is used by setup tools to define the configurations of the project , such as metadata , dependencies and more.

"""

from setuptools import find_packages, setup #considers folders with __init__ file as a package
from typing import List


def get_requirements()->List[str]:

    """
    
    This function will return list of requirements
    
    """

    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:

            lines=file.readlines()

            for line in lines:
                requirement=line.strip()
                #ignore empty lines and -e .(-e . in requirements.txt triggers the setup.py file)
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)


    except FileNotFoundError:
        print('Requirements.txt file not found')

    return requirement_lst

setup(
    name='NetworkSecurty',
    version='0.0.1',
    author='Anirban Chatterjee',
    packages=find_packages(),
    install_requires=get_requirements()
)

