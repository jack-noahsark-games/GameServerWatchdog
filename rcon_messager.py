from rcon.source import Client
import schedule
import time


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


def send_warning_message(rcon_servers,details):
    try:
        rcon_ip = details["rcon_ip"]
        rcon_port = details["rcon_port"]
        rcon_password = details["rcon_password"]
        
        with Client(rcon_ip, rcon_port, passwd=rcon_password) as client:
            response = client.run(f"say Restarting server in 15 minutes.")
            time.sleep(300)
            response = client.run(f"say Restarting server in 10 minutes.")
            time.sleep(300)
            response = client.run(f"say Restarting server in 5 minutes.")
            time.sleep(240)
            response = client.run(f"say Restarting server in 1 minutes.")
            time.sleep(30)
            response = client.run(f"say Restarting server in 30 seconds.")
            time.sleep(30)
            response = client.run(f"say Restarting server now, please exit the server.")
            time.sleep(10)
                
    except Exception as e:
        print(f"Failed to send command")
        
        
        

schedule.every().day.at("10:30").do(send_warning_message)    
