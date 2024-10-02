import psutil
import subprocess
import schedule
import time
 
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

def is_process_running(process_name):
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name']== process_name:
                print(f"{process_name} is running, checking again in 30 seconds.")                
                return True
        print(f"{process_name} is not running.")        
        return False

def attempt_process_start(process_name, details):
    
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
            try:
                process_path = details["process_path"]
                working_directory = details["working_directory"]
                print(f"Attempting to start {process_name} now, waiting...")
                process_start = subprocess.Popen(process_path, cwd=working_directory)
                time.sleep(3)
                
                if is_process_running(process_name):
                    print(f"{process_name} has successfully started on retry.")
                    break
                else:
                    print(f"An error occured whilst attempting to open {process_name}, trying again.")
                    attempts += 1
            except Exception as e:
                print(f"Failed to start with exception code, {e}")
                if attempts >= max_attempts:
                    print(f"Maximum attempts reached for {process_name}. Moving onto next process")
                
def process_monitor():
    for process_name, details in processes.items():
        if not is_process_running(process_name):
            attempt_process_start(process_name, details)
        
process_monitor()     
schedule.every(1).minutes.do(process_monitor)  

while True:
    schedule.run_pending()
    time.sleep(1)