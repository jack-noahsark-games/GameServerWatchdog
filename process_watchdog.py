import psutil
import os
import subprocess
process_name = "Discord.exe"
discord_path = r"C:\Users\jack1\AppData\Local\Discord\app-1.0.9164\Discord.exe"
working_directory = r"C:\Users\jack1\AppData\Local\Discord\app-1.0.9164"
def game_server_check():
    process_running = False
    
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            print(f"{process_name} is running")
            process_running= True
            break
        
    if process_running:
        print(f"{process_name} is running.")
    else:
        print(f"{process_name} is not running, restarting now.")
        
        process_start = subprocess.call(discord_path, cwd=working_directory)
        if process_start == 0:
            print("Process successfully started")
        else:
            print ("Process failed with return code", process_start)
                  
game_server_check()