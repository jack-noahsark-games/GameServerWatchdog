import psutil
import subprocess
import schedule
import time
process_name="Discord.exe"
process_path = r"C:\Users\jack1\AppData\Local\Discord\app-1.0.9164\Discord.exe"
working_directory = r"C:\Users\jack1\AppData\Local\Discord\app-1.0.9164"

def is_process_running():
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name']== process_name:
            print(f"{process_name} is running, checking again in 30 seconds.")
            return True
        
    return False #we put return False here because if we put it as else: false, it only checks one process in the for loop and terminates early



def attempt_process_start(): 
    
    attempts = 0
    max_attempts = 2
    
    while attempts < max_attempts:
        try:
            print(f"{process_name} is not running, attempting to restart now.")
            process_start = subprocess.Popen(process_path, cwd=working_directory)
            time.sleep(10)
            
        
            if is_process_running():
                print("Process successfully started")
                return True
            else:
                print(f"An error occured when attempting to open {process_name}.")
                attempts += 1

        except Exception as e:
            print(f"Failed to start with exception code", e)
            attempts += 1
  

def process_monitor():
    if not is_process_running():
        if not attempt_process_start():
            print("Terminating script due to repeated failures.")
            exit()

process_monitor()  
schedule.every(1).minutes.do(process_monitor)  

while True:
    schedule.run_pending()
    time.sleep(1)
    
processes = {
    "Discord.exe":{
        "path": r"C:\Users\jack1\AppData\Local\Discord\app-1.0.9164\Discord.exe",
        "working_directory": r"C:\Users\jack1\AppData\Local\Discord\app-1.0.9164"
    },

    "Chrome.exe":{
        "path": r"C:\Program Files\Google\Chrome\Application\Chrome.exe",
        "working_directory": r"C:\Program Files\Google\Chrome\Application"
    },
    
    "waterfox.exe":{
        "path": r"C:\Program Files\Waterfox\waterfox.exe",
        "working_directory": r"C:\Program Files\Waterfox"
    }
}

def is_process_running():
    for process_name in processes: #this only acccesses the outer dictionary.
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name']== {processes}:
                print(f"{process_name} is running, checking again in 30 seconds.")
                return True
        
    return False #we put return False here because if we put it as else: false, it only checks one process in the for loop and terminates early





    
        

    
        
            
        