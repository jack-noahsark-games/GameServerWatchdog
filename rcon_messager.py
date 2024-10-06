from rcon.source import Client
import datetime
import schedule
message_times = ["08:00", "12:00", "18:00" , "00:00"]

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

time_to_restart = datetime.datetime.now()
warning_message = "Warning: Server will restart in {time_to_restart} minutes"
def send_warning_message(rcon_servers,details):
    try:
        rcon_ip = details["rcon_ip"]
        rcon_port = details["rcon_port"]
        rcon_password = details["rcon_password"]
        
        with Client(rcon_ip, rcon_port, passwd=rcon_password) as client:
            response = client.run(f"say {warning_message}")
        
        
    except Exception as e:
        print(f"Failed to send command")
        
        
        

schedule.every().day.at("10:30").do(send_warning_message)    
