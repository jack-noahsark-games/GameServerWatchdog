from rcon.source import Client

rcon_servers = {
    
    "ark":{
        "rcon_ip" : "192.168.0.1",
        "rcon_port" : 207405,
        "rcon_password" : "test1"
    },
    "minecraft":{
        "rcon_ip" : "192.168.0.1",
        "rcon_port" : 207406,
        "rcon_password" : "test2"
    },
    "csgo":{
        "rcon_ip" : "192.168.0.1",
        "rcon_port" : 207407,
        "rcon_password" : "test3"
        
    }
}

class rcon_connection():
    with Client(rcon_ip,rcon_port,passwd = rcon_password) as client:
        rcon_ip = rcon_servers["ark"]["rcon_port"]
        rcon_port = rcon_servers["ark"]["rcon_port"]
    