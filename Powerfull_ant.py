#!/usr/bin/python3

import os , threading , urllib , nmap , re , validators , argparse
from termcolor import colored
from urllib.request import urlopen
from socket import *
from threading import *
from nmap import *


def Port_Scan(ip,Port):

    try:
        result = nm.scan(ip, str(Port))
        port_status = (result['scan'][ip]['tcp'][Port]['state'])
        if port_status == "open" or port_status == "filtered":
            proto = (getservbyport(Port, str(proto)))
            reason = nm[ip]['tcp'][Port]['reason']
            while a == 0:
                pass
            else:
                print(colored(f"[+] {proto} Port {Port} is {port_status} and on Running on {a} Service in Target Machine","green"))
            
            if c == 0:
                c = 1

    except:
        print(colored(f"[-] Cannot Scan Port {port}", "red"))

def check_ip(ip):
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if(re.search(regex, ip)):
        return 1
    
def OS_dection(ip):
    machine = nm.scan(ip, arguments='-O')
    Os = (machine['scan'][ip]['osmatch'][0]['osclass'][0]['osfamily'])
    print(colored(f"[+] The Operating System of Target Machine is {Os} OS","green"))
    a = 1


try:
    urlopen('https://www.google.com')
except urllib.error.URLError as Error:
    print(colored("[-] Internet is not Connected", "red"))
    exit()

os.system("clear")

while True:
    
    try:
        ip = str(input(colored("[!] Enter Target's IP or DNS Name :", "blue")))
        if check_ip(ip) == 1:
            break

        elif validators.domain(ip) == True:
            ip = gethostbyname(ip)
            break
    
    except:
        print(colored("[-] IP Addres or DNS Name is Invalid", "red"))

a = 0
c = 0
Port = 0
nm = nmap.PortScanner()
proto = nm[str(ip)].all_protocols()
parser = argparse.ArgumentParser()
args = parser.parse_args()
t1 = threading.Thread(target= Port_Scan, args= (ip, Port), daemon=True)
t2 = threading.Thread(target= OS_dection, args= (ip, Port), daemon=True)
parser.add_argument("-FS", "--FastScan" , help="Scans Ports in Fast mode" , action="store_const" , const=1)
parser.add_argument("-AS", "--AggrasiveScan" , help="Scans Ports in Aggrasive mode" , action="store_const" , const=1)

t2.start()
    
else:
    a = 1

if args.AggrasiveScan == 1:
    for Port in range(0,65536):
        if KeyboardInterrupt():
            break
        t1.start()

if args.FastScan == 1:
    minimum = int(input(colored("[!] Enter minimum Port For Scan :\n", "blue")))
    maximum = int(input(colored("\n[!] Enter maximum Port For Scan :\n", "blue")))

    for Port in range(minimum,maximum):
        if KeyboardInterrupt():
            break
        t1.start()

t1.join()

if c == 0:
    print(colored(f"[-] Any Port is not Open on IP {ip}","red"))

