import re
import os
import time

def main():
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
    # os.system("git add .")
    # os.system("git commit -am update")
    # os.system("git push")

if __name__ == "__main__":
    while(1):
        main()
        time.sleep(600)