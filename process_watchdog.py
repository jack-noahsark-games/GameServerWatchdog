import psutil
import subprocess
import schedule
import time
#dictionary that holds processes we want to monitor
#each process holds two key attributes
#process path - directions for the script to execute process
#working_directory - where it runs, for script to navigate to proper directory.
processes = {
    "Discord.exe":{
        "process_path": r"C:\Users\jack1\AppData\Local\Discord\app-1.0.9164\Discord.exe",
        "working_directory": r"C:\Users\jack1\AppData\Local\Discord\app-1.0.9164"
    },

    "chrome.exe":{
        "process_path": r"C:\Program Files\Google\Chrome\Application\Chrome.exe",
        "working_directory": r"C:\Program Files\Google\Chrome\Application"
    },
    
    "waterfox.exe":{
        "process_path": r"C:\Program Files\Waterfox\waterfox.exe",
        "working_directory": r"C:\Program Files\Waterfox"
    }
}

#function to check if a process is running by its name in tsk mngr
#looks through all system processes to find a match (ps.util.process_iter)

def is_process_running(process_name):
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name']== process_name:
                print(f"{process_name} is running, checking again in 30 seconds.")                
                return True
        print(f"{process_name} is not running.")        
        return False

#function to attempt starting a process that was not found in is_process_running, tries up to 3 times.
def attempt_process_start(process_name, details):
    
    max_attempts = 3 #amount of attempts allowed before moving along
    attempts = 0
    #keep trying to open process utnil we hit maximum number of attempts
    while attempts < max_attempts:
            try:
                process_path = details["process_path"]#grab path of executable
                working_directory = details["working_directory"]#get the working directory
                print(f"Attempting to start {process_name} now, waiting...")
                process_start = subprocess.Popen(process_path, cwd=working_directory)
                time.sleep(3)#give it 3 seconds before checking if its running again (otherwise it falsely marks it as not running if there is no wait time)
                
                #recheck if process is running
                if is_process_running(process_name):
                    print(f"{process_name} has successfully started on retry.")
                    break #exit this loop if the process is running
                else:
                    print(f"An error occured whilst attempting to open {process_name}, trying again.")
                    attempts += 1 #incremenet attempts until 3 tries reached if no process running even after reattempt to open
            except Exception as e:
                print(f"Failed to start with exception code, {e}")
                attempts += 1 #incremements if error occurs.
                if attempts >= max_attempts:
                    print(f"Maximum attempts reached for {process_name}. Moving onto next process")

#main monitoring function that calls the functuions that checks and restarts processes             
def process_monitor():
    for process_name, details in processes.items():
        if not is_process_running(process_name): #if process not running
            attempt_process_start(process_name, details) #try to start it (with attempt_process_start)
        
process_monitor()#this is here purely for testing rather than waiting 1 minute
schedule.every(1).minutes.do(process_monitor)#this is the only one we need for when i am ready to release

#keep script runnin indefenitely, checking the schedule for pending tasks
while True:
    schedule.run_pending() #run scheduled jobs if the time has come
    time.sleep(1) #wait for 1 second before the next loop iteration here