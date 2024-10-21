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

abort = False
flag = False

def abort_check():
    global abort, flag


    while True:
        print("abort_check started")
        user_input = input(f"Would you like to abort this wait: y/n?")
        
        if user_input.lower() == "y":
            abort = True
            print("Aborting...")
        
        elif flag:
            print("Flag is true, for loop finished, abort_check restarting now and waiting for the next for loop to finish")
            flag = False
            time.sleep(5)

        elif user_input == "n":
            print("Script will continue to wait...")
        else:
            print(f"{user_input} is not a valid character, please choose y or n: ")

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
        global abort, flag
        rcon_ip = server_details["rcon_ip"]
        rcon_port = server_details["rcon_port"]
        rcon_password = server_details["rcon_password"]
        
        
        
        for minutes, rcon_message in countdown_messages:               
            chat_feedback = f"say {rcon_message}"
            print(f"Next iteration {minutes}")
            if minutes >= 5:
                print(chat_feedback)
                for _ in range(30):
                    print("10 seconds wait")
                    time.sleep(10)
                    if abort:
                        abort = False
                        print(abort)
                        print("Wait aborted during countdown")
                        break
                else:
                    flag = True
                    
            elif minutes >= 1:
                print(chat_feedback)
                for _ in range(6):
                    print("10 seconds wait")
                    time.sleep(10)
                    if abort:
                        print("Wait aborted during countdown")
                        abort = False
                        break
                else:
                    flag = True  
                                  
            elif minutes >= 0.5:
                print(chat_feedback)    
                for _ in range (3):
                    print("10 seconds wait")
                    time.sleep(10)
                    if abort:
                        abort = False
                        print("Wait aborted during countdown")
                        break
                else:
                    flag = True
                
            elif minutes == 0:
                print(chat_feedback)
                for _ in range (3):   
                    time.sleep(10)
                    if abort:
                        abort = False
                        print("Wait aborted during countdown")
                        break
                else:
                    flag = True
                    
    except Exception as e:
        print(f"failed with {e}")
    finally:
        abort = False
        
threading.Thread(target=abort_check, daemon=True).start()


send_warning_message(rcon_servers["minecraft"])
schedule.every().day.at("06:00").do(lambda: send_warning_message(rcon_servers["minecraft"]))
schedule.every().day.at("12:00").do(lambda: send_warning_message(rcon_servers["minecraft"]))

while True:
    schedule.run_pending()
    time.sleep(1)