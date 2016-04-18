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
    os.system("ifconfig ppp1 | cat >> ifconfig.out")
    os.system("ifconfig en0 | cat >> ifconfig.out")
    os.system("ifconfig en1 | cat >> ifconfig.out")
    os.system("ifconfig en2 | cat >> ifconfig.out")
    f = open("ifconfig.out")
    s = f.read(100000)
    p = re.findall(re.compile("[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*"), s)
    f.close()
    os.system("ifconfig | cat > ifconfig.out")
    ifconfig = open("ifconfig.out").read(100000)
    os.system("rm ip.out")
    ipf = open("ip.out", 'w')
    ipf.write(p[0])
    ipf.close()

    baidu_ip = requests.get("http://www.baidu.com/s?wd=ip").text
    ip_filter = re.compile("[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+")
    ip_out = re.findall(ip_filter, baidu_ip)[0]

    server_addr = "http://"+config['server']+":"+str(config['port'])
    if old_p != p[0]:
        requests.post(server_addr, data=json.dumps({config['machine_name']: {"ip": p[0], "ipo": ip_out, "if": ifconfig}}))
        old_p = p[0]

if __name__ == "__main__":
    while(1):
        try:
            main()
            time.sleep(config["timeout"])
        except Exception as e:
            print e
