import json
from datetime import datetime
import os


def get_configObj():
    f = open('config.json')
    data = json.load(f)
    f.close()
    return data

def formatDate():
    formatedDate = datetime.now().strftime("%d-%b-%Y")
    format = "\n"*10+"="*20 + " " + formatedDate + " " + "="*20
    return format

def load_file():
    config = get_configObj()
    formatDate_ = formatDate()
    checkDate = True
    if os.path.exists(config["file_path"]) == False:
        f = open(config["file_path"], "a")
        f.close()

    with open(config["file_path"],"r") as f:
        fileLine = f.readlines()
        if len(fileLine)>0:
            if formatDate_.replace("\n","") == fileLine[-1]:
                checkDate = False
    if checkDate:
        
        with open(config["file_path"],"a") as f:
            f.write(formatDate_)
 
load_file()