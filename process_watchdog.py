import psutil
import os
import subprocess
process_name = "Discord.exe"
discord_path = r"C:\Users\jack1\AppData\Local\Discord\app-1.0.9164\Discord.exe"
working_directory = r"C:\Users\jack1\AppData\Local\Discord\app-1.0.9164"
def game_server_check():
    process_running = False
    
    for process in psutil.process_iter(['pid', 'name']): #iterates over the existin PID's + corresponding process names, name is not specified yet.
        if process.info['name'] == process_name: #states that as it itertes, if a name of process (discord) is found, print process_ running
            print(f"{process_name} is running")
            process_running= True
            break
        
    if process_running == False:
        print(f"{process_name} is not running, restarting now.")
        
        process_start = subprocess.run(discord_path, cwd=working_directory) #if process running, attempt to start program | cwd = working directory | discord_path is just the path of the .exe
        stdout = subprocess.DEVNULL
        stderr = subprocess.DEVNULL
        if process_start == 0:
            print("Process successfully started")
            
            
        else:
            print ("Process failed with return code", process_start.returncode)
            process_start = subprocess.run(discord_path, cwd=working_directory) #2nd attempt to start process            
            if process_start == 0:
                print("On retry, the process started")
                
            else:
                print("Process did not start on two attempts and returned with error code", process_start.returncode,".","Please check if you can start this process manually.")

                  
game_server_check()


#the issue i run into here, is that with subprocess.run, it waits for the program to start which is good, and it reacts to the application closing, which is fit for purpose.
#but when we close the script, it closes the application too. because this is how subprocess.run works.
#however, if we use subprocess.Popen, the .exe does not close when script closes BUT there are two issues


#1st issue, the script no longer is able to feedback to user that the process is open, when running subprocess.Popen
#2nd issue, the script no longer reopens that application if it crashes, if using Popen, which for a watchdog script, is not working as intended.