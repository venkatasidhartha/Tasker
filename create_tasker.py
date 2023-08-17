import os
import json
import datetime

def create_tasker_file():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    config_file = open(f"{os.getcwd()}/config.json")
    configuration = json.load(config_file)
    filepath = os.path.join(configuration["path"],configuration["folder_name"])
    check_fileExist = os.path.exists(filepath) 
    if not check_fileExist:
        os.makedirs(filepath)
    formatedDate = datetime.datetime.now().strftime("%d-%b-%Y")
    current_dateFile = f'{formatedDate}.txt'
    format = "="*20 + formatedDate + "="*20
    file = os.path.join(filepath,current_dateFile)
    if not os.path.exists(file):
        with open(os.path.join(filepath,current_dateFile),"a") as f:
            f.write(format)
    return filepath

if __name__ == '__main__':
    create_tasker_file()

   
