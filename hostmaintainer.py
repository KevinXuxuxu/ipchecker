import os
import requests
import time
import json

config = json.load(open("config.json"))
d_old = {}

def update(d):
	f = open("/etc/hosts")
	lines = f.readlines()
	f.close()
	tuples = [p.strip().split('\t') for p in lines if not (p.startswith('#') or p.startswith(":"))]
	for (ip, name) in tuples:
		if name not in d.keys():
			d[name] = {"ip": ip}
	new_lines = [l for l in lines if (l.startswith('#') or l.startswith(':'))] + [d[name]["ip"]+'\t'+name+'\n' for name in d.keys()]
	f = open("/etc/hosts", 'w')
	f.writelines(new_lines)
	f.close()

def main():
	global d_old
	server_addr = "http://"+config['server']+":"+str(config['port'])
	rep = requests.get(server_addr)
	raw = rep.text.replace("\'", "\"").replace("u\"", "\"")
	d = json.loads(raw)
	if d != d_old:
		print d
		print
		update(d)
		d_old = d

if __name__ == "__main__":
	while True:
		try:
			main()
			time.sleep(config["timeout"])
		except Exception as e:
			print time.ctime() + ": " + e.message
