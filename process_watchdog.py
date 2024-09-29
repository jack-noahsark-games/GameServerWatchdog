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
    
        print(f"{process_name} is not running, attempting to restart now.")
        process_start = subprocess.Popen(process_path, cwd=working_directory)
        return_code = process_start.returncode
        time.sleep(5)
        
        if return_code == 0:
            print("Process successfully started")
            return True
        else:
            print("Process failed with return code", process_start.returncode)
            process_start = subprocess.Popen(process_path, cwd=working_directory)
            return_code = process_start.returncode
            time.sleep(5)

            if return_code != 0:
                print(f"{process_name} failed to start on two occassions, with {return_code}, please check if you can open this process manually.")
                return False
            return True
  

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
    
#cleaned up functions but still not working properly, the process is not recognising that the process is open, need to revisit


    
        

    
        
            
        