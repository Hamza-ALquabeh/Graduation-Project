TARGET_SUBNET = "192.168.1.0/24"
import nmap 



outputfile = "scan_results.txt"



#Port scanning function that takes a host and performs a vulnerability port scan on it
def port_scan(host):
    scanner = nmap.PortScanner()
    results=scanner.scan(hosts = host, arguments= f"-vv -sN --host-timeout 5m -script vuln")
    data = scanner.csv()
    ports=0
    f = open(outputfile,'a')
    for service in data.split('\n')[1:-1]:
        try:
            split = service.split(';')
            serv = split[5]
            if serv =="":
                serv = "-"
            port = split[4]
            f.write(f"Service/port: {serv}/{port}\n")
            ports+=1
    
        except Exception as e1:
            f.write(f"Error occured {e1}\n")
            pass
        
    script_check = False
    try:
        for port in results["scan"][host]["tcp"]:
            try:
                for key in results["scan"][host]["tcp"][port]["script"]:
                    f.write(f"{port}- {key}: {results['scan'][host]['tcp'][port]['script'][key]}\n")
                    script_check = True
            except:pass
    except:pass
    
    try:
        for port in results["scan"][host]["udp"]:
            try:
                for key in results["scan"][host]["udp"][port]["script"]:
                    f.write(f"{port}- {key}: {results['scan'][host]['udp'][port]['script'][key]}\n")
                    script_check = True
            except:pass 
    except:pass
    if not script_check:
        f.write(f"Scripts found no vulnerabilities\n")
        
    if ports == 0:
        f.write(f"No ports open\n")
    else:
        f.write(f"Total number of open ports: {ports}\n")


#Network host discovery scan that takes in one of 4 options (IP, ICMP,Timestamp or Netmask) and returns list of alive hosts and their total
def scan(mode = ''):
    f = open(outputfile, "a")
    opt = ""
    if mode.lower().startswith("ip"):
        opt = "-PO"
        f.write(f"IP protocol Scanner running...\n")
    elif mode.lower().startswith("net"):
        opt = "-PM"
        f.write(f"Netmask Scanner running...\n")
    elif mode.lower().startswith("time"):
        opt = "-PP"
        f.write(f"Timestamp Scanner running...\n")
    else:
        f.write(f"ICMP Scanner running...\n")
        
    scanner = nmap.PortScanner()
    scanner.scan(hosts = TARGET_SUBNET, arguments=f'-sn -vv {opt} ')
    
    hosts = 0
    output = []
    for host in scanner.all_hosts():
        if scanner[host].state()=='up':
            output.append(host)
            hosts +=1  
    return output


def main(target_subnet = TARGET_SUBNET):
    f = open(outputfile, 'w')
    hosts = scan("ip")
    for host in hosts:
        f.write(f"host {host} is up\n")
        f.write(f"Running port scanner on host {host}...\n")
        port_scan(host)
        f.write('\n')
    f.write(f"Total number of hosts alive: {len(hosts)}\n")
main()
