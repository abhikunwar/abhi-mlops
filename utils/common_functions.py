# read_yml,create_path
import yaml
import os

def read_yml(yaml_file_name):
    yaml_file_path = os.path.join('config',yaml_file_name)
    with open(yaml_file_path,'r') as f:
        file = yaml.safe_load(f)
    return file
def create_dir(folder_path):
    # dir_path = os.path.join(root_dir,dir_path)
    os.makedirs(folder_path,exist_ok = True)


