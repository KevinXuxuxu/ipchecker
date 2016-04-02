import re
import os
import time
import json
import requests

# necessary keys in config: server, port, machine_name
config = json.load(open("config.json"))
old_p = "whatever"

def main():
    global old_p
    os.system("rm ifconfig.out")
    os.system("ifconfig ppp0 | cat >> ifconfig.out")
    os.system("ifconfig en0 | cat >> ifconfig.out")
    os.system("ifconfig en1 | cat >> ifconfig.out")
    os.system("ifconfig en2 | cat >> ifconfig.out")
    f = open("ifconfig.out")
    s = f.read(100000)
    p = re.findall(re.compile("[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*"), s)
    f.close()
    os.system("rm ip.out")
    ipf = open("ip.out", 'w')
    ipf.write(p[0])
    ipf.close()

    server_addr = "http://"+config['server']+":"+str(config['port'])
    if old_p != p[0]:
        requests.post(server_addr, json={config['machine_name']: p[0]})
        old_p = p[0]

if __name__ == "__main__":
    while(1):
        main()
        time.sleep(config["timeout"])
