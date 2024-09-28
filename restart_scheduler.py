from datetime import datetime 
import schedule
import os
import shutil

#schedule back up job
#schedule restart
#schedule RCON messages

def schedule_backup():
    schedule.every().day.at("10:30").do(backup.py)
    
def schedule_restart():
    schedule.every().day.at("10:30").do(restart.py)
