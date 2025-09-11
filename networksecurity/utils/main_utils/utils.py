import yaml
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging  
import os
import sys
import numpy as np
import dill
import pickle

def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and returns its contents as a dictionary.

    Args:
        file_path (str): The path to the YAML file.

    Returns:
        dict: The contents of the YAML file as a dictionary.

    Raises:
        NetworkSecurityException: If there is an error reading the file.
    """
    try:
        with open(file_path, 'r') as file:
            content = yaml.safe_load(file)

        print(f"YAML file '{file_path}' read successfully.")
        logging.info(f"YAML file '{file_path}' read successfully.")
        return content
    except Exception as e:
        raise NetworkSecurityException(e, sys) 
    

def write_yaml_file(file_path:str, content: object, replace:bool=False)->None:
    """
    Writes a dictionary to a YAML file.

    Args:
        file_path (str): The path to the YAML file.
        content (dict): The dictionary to write to the file.

    Raises:
        NetworkSecurityException: If there is an error writing to the file.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            yaml.dump(content, file)

        print(f"YAML file '{file_path}' written successfully.")
        logging.info(f"YAML file '{file_path}' written successfully.")
    except Exception as e:
        raise NetworkSecurityException(e, sys)