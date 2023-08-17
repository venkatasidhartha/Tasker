import os
import sys
import json
from crontab import CronTab
from create_tasker import create_tasker_file

def remove_jobExist(cron,command):
    for job in cron:
        if job.command == command:
            cron.remove(job)
            break

def get_pathDetials():
    pathInput = input("Enter The Path to save folder >>> ")
    if pathInput == "" or not os.path.exists(pathInput):
        # print("Path is Incorrect")
        sys.stdout.write("Path is Incorrect")
        get_pathDetials()
    foldernameInput = input("Enter The Folder Name to save files >>> ")
    if foldernameInput == None or foldernameInput == "":
        # print("Folder Name is Incorrect")
        sys.stdout.write("Folder Name is Incorrect")
        get_pathDetials()
    config = {
            "path":pathInput, 
            "folder_name":foldernameInput
        }
    with open("config.json","w") as f:
        json.dump(config,f)
    folder = create_tasker_file()
    cronjob_10AM()
    sys.stdout.write(f"Folder Created in This Path >> {folder}")


def set_cronjob_reboot():
    current_username = os.getlogin()
    cron = CronTab(user=current_username)  
    command_ = f'python3 {os.getcwd()}/create_tasker.py >> {os.getcwd()}/logger.log 2>&1'
    remove_jobExist(cron,command_)
    job = cron.new(command=command_)
    job.setall('@reboot')
    cron.write() 

def cronjob_10AM():
    set_cronjob_reboot()
    current_username = os.getlogin()
    cron = CronTab(user=current_username)  
    command_ = f'python3 {os.getcwd()}/create_tasker.py >> {os.getcwd()}/logger.log 2>&1'
    remove_jobExist(cron,command_)
    job = cron.new(command=command_)
    # Set the schedule for the cron job (e.g., run every day at 10 AM)
    job.setall('0 10 * * *')
    
    cron.write() 





get_pathDetials()