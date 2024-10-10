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

def send_warning_message(server_details):
    try:
        #these variables are not relevant for this current testing purpose, but once we switch from print to rcon.client(run) they will become relevant
        rcon_ip = server_details["rcon_ip"]
        rcon_port = server_details["rcon_port"]
        rcon_password = server_details["rcon_password"]
        
        #with Client(rcon_ip, rcon_port, passwd=rcon_password) as client:
        for minutes, rcon_message in countdown_messages:
                
            chat_feedback = f"say {rcon_message}"
            skip_input = ""
                
            if minutes >= 5:
                print(chat_feedback)
                skip_input = input("Would you like to abort this wait: y/n?")
                if skip_input == "y":
                    print("Wait aborted, moving on...")
                else:
                    time.sleep(300)
                
            elif minutes >= 1:
                print(chat_feedback)
                skip_input = input("Would you like to abort this wait: y/n?")
                if skip_input == "y":
                    print("Wait aborted, moving on...")
                else:
                    time.sleep(60)
                
            elif minutes >= 0.5:
                print(chat_feedback)
                skip_input = input("Would you like to abort this wait: y/n?")
                if skip_input == "y":
                    print("Wait aborted, moving on...")
                else:
                    time.sleep(30)
                
            elif minutes == 0:
                print(chat_feedback)
                time.sleep(10)
                print(f"Server shutting down now...")
                time.sleep(30)
                
    except Exception as e:
        print(f"failed with {e}")        
        

    
send_warning_message(rcon_servers["minecraft"])
schedule.every().day.at("06:00").do(lambda: send_warning_message(rcon_servers["minecraft"]))
schedule.every().day.at("12:00").do(lambda: send_warning_message(rcon_servers["minecraft"]))

while True:
    schedule.run_pending()
    time.sleep(1)