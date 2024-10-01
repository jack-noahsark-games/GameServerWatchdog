import psutil
import subprocess
import schedule
import time
 
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
        found = False
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name']== process_name:
                print(f"{process_name} is running, checking again in 30 seconds.")
                found = True
                break
            if not found:
                print(f"{process_name} is not running.")
        
    return False #we put return False here because if we put it as else: false, it only checks one process in the for loop and terminates early

is_process_running()





    
        

    
        
            
        