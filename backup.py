import os
import shutil
from datetime import datetime
import schedule
import time

#gets the current date and time in 31/07/22 - 12:00:01 format, to rename the folder below when backing up to give a tiem of the backup
current_time = datetime.now().strftime('%d-%m-%y --- %I.%M.%S%p')

#src_backup & dst_backup are the filepaths to the folder we wish to back up
src_backup = r'C:\Users\jack1\Documents\Python projects\source'
dst_backup = r'C:\Users\jack1\Documents\Python projects\destination\backup'

#current_naming just takes the current name of the newly backed up file, and renames it to new_naming
current_naming= r'C:\Users\jack1\Documents\Python projects\destination\backup'
new_naming = fr'C:\Users\jack1\Documents\Python projects\destination\{current_time}'



def backup_process():
    shutil.copytree(src_backup, dst_backup) #copies files from source into dest
    os.rename(current_naming, new_naming)  #renames the new "backup" folder to have a naming convention that follows date + time for readability.


schedule.every().day.at("06:00").do(backup_process)
schedule.every().day.at("12:00").do(backup_process)
schedule.every().day.at("18:00").do(backup_process)
schedule.every().day.at("00:00").do(backup_process)

while True:
    schedule.run_pending()
    time.sleep(1)
    

