import subprocess
import optparse 
from re

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface", help="interface to change mac address")
    parser.add_option("-m","--mac", dest="mac", help="new mac address")
    (options, arguments)= parser.parse_args()
    if not options.interface:
        parser.error("[-]Please enter interface to change the mac address")
    elif not options.mac:
        parser.error("[-]Please specify new mac address")
    return options
        
def mac_changer(interface,mac):
    print("[+] MAC address of "+ options.interface + " changed to "+ options.mac)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac])
    subprocess.call(["ifconfig",interface,"up"])
    
options= get_argument()
mac_changer(options.interface,options.mac)

#ifconfig_result= subprocess.check_output(["ifconfig", options.interface])
#macsr = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)

