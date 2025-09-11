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
    

def save_numpy_array_data(file_path:str, array:np.array)->None:
    """
    Saves a numpy array to a file.

    Args:
        file_path (str): The path to the file where the array will be saved.
        array (np.array): The numpy array to save.

    Raises:
        NetworkSecurityException: If there is an error saving the array.
    """
    try:
        dir_path = os.path.dirname(file_path)   #create directory path
        os.makedirs(dir_path, exist_ok=True)     #make that directory in the above path if not exists
        with open(file_path, 'wb') as file_obj:            
            np.save(file_obj, array)               #save numpy array to that file

        print(f"Numpy array saved successfully at '{file_path}'.")
        logging.info(f"Numpy array saved successfully at '{file_path}'.")
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e
    
def save_object(file_path:str, obj:object)->None:
    """
    Saves a Python object to a file using dill.

    Args:
        file_path (str): The path to the file where the object will be saved.
        obj (object): The Python object to save.

    Raises:
        NetworkSecurityException: If there is an error saving the object.
    """
    try:
        logging.info("Entered the save_object method of utils")
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

        print(f"Object saved successfully at '{file_path}'.")
        logging.info(f"Object saved successfully at '{file_path}'.")
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e