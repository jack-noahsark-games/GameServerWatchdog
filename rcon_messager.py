from rcon.source import Client
import schedule
import time
import threading


rcon_servers = {
    
    "ark":{
        "rcon_ip" : "192.168.0.1",
        "rcon_port" : 207405,
        "rcon_password" : "test1"
    },
    "minecraft":{
        "rcon_ip" : "192.168.0.1",
        "rcon_port" : 207406,
        "rcon_password" : "test2",
    },
    "csgo":{
        "rcon_ip" : "192.168.0.1",
        "rcon_port" : 207407,
        "rcon_password" : "test3"
        
    }
}



countdown_messages = [ #dictionary for the countdown messages, purpose - iterating through them
        (15, "Restarting server in 15 minutes."),
        (10, "Restarting server in 10 minutes."),
        (5, "Restarting server in 5 minutes."),
        (1, "Restarting server in 1 minute."),
        (0.5, "Restarting server in 30 seconds."),
        (0, "Restarting server now, please exit the server.")
        
    ]

abort = False

def abort_check():
    global abort
    while not abort:
        user_input = input(f"Would you like to abort this wait: y/n?")
        if user_input.lower() == "y":
            abort = True
            print("Aborting...")
        elif user_input == "n":
            print("Script will continue to wait...")      
        else:
            print("Please choose a valid input: y/n ...")   

def send_warning_message(server_details):
    global abort
    try:
        abort = False
        #these variables are not relevant for this current testing purpose, but once we switch from print to rcon.client(run) they will become relevant
        rcon_ip = server_details["rcon_ip"]
        rcon_port = server_details["rcon_port"]
        rcon_password = server_details["rcon_password"]
        

        
        #with Client(rcon_ip, rcon_port, passwd=rcon_password) as client:
        for minutes, rcon_message in countdown_messages:
                
            chat_feedback = f"say {rcon_message}"
            
            if abort:
                print("Wait aborted, moving on...")
                return
            
            print(chat_feedback)
                
            if minutes >= 5:
                for _ in range(30):
                    time.sleep(10)
                    if abort:
                        print("Wait aborted during countdown")
                        return
                    
            elif minutes >= 1:
                for _ in range(6):
                    time.sleep(10)
                    if abort:
                        print("Wait aborted during countdown")
                        return
                
            elif minutes >= 0.5:
                for _ in range (3):
                    time.sleep(10)
                    if abort:
                        print("Wait aborted during countdown")
                        return
                
            elif minutes == 0:
                for _ in range (3):   
                    time.sleep(10)
                    if abort:
                        print("Wait aborted during countdown")
                        return
                
    except Exception as e:
        print(f"failed with {e}")        
    finally:
        abort = False
        

threading.Thread(target=abort_check, daemon=True).start() #daemon threads run in the background and automatically terminate when the main progam finishes. It ensures
        #the background thread does not block the program from exiting once all non-daemon threads (like the main thread) are done    
    
send_warning_message(rcon_servers["minecraft"])
schedule.every().day.at("06:00").do(lambda: send_warning_message(rcon_servers["minecraft"]))
schedule.every().day.at("12:00").do(lambda: send_warning_message(rcon_servers["minecraft"]))

while True:
    schedule.run_pending()
    time.sleep(1)