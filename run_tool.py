#This script is responsible for running the following:
#1- Run snort
#2- Run u2json 
#3- Run filebeat
#4- Run packetbeat
#5- Scan
#6- Threat int
#7- snort alert 

import subprocess


def Snort():
    interface = input("Interface name (leave empty if default)")
    try:
        if interface =="":
            subprocess.Popen(["snort","-d", "-c", "/etc/snort/snort.conf"])
        else:
            subprocess.Popen(["snort", "-c","-d", "/etc/snort/snort.conf", "-i", interface])
    except Exception as e:
        print(f"Error occured while running Snort {e}")

def filebeat():
    try:
        # subprocess.Popen(["cd", "/home/doffy/filebeat-8.13.4-linux-x86_64"])

        subprocess.Popen(["/home/doffy/filebeat-8.13.4-linux-x86_64/filebeat", "run", "--path.config", "/home/doffy/filebeat-8.13.4-linux-x86_64"])
    except Exception as e:
        print(f"Error occured while running Filebeat {e}")

def u2json():
    try:
        subprocess.Popen(["idstools-u2json", "--snort-conf", "/etc/snort/snort.conf", "--directory", "/var/log/snort",
                        "--prefix", "snort.log", "--follow", "--output", "/var/log/snort/snort.json"])
    except Exception as e:
        print(f"Error occured while running U2json {e}")

def scan():
    try:
        subprocess.Popen(["python3", "/home/doffy/Desktop/GP/nmap_scan.py"])

    except Exception as e:
        print(f"Error occured while running scan {e}")

def threat():
    try:
        subprocess.Popen(["python3", "/home/doffy/Desktop/GP/threat.py"])
    except Exception as e:
        print(f"Error occured while running threat intelligence script {e}")

def snort_alert():
    try:
        subprocess.Popen(["python3", "/home/doffy/Desktop/GP/snort_alert.py"])
        print(f"Alert script successfully running")
    except Exception as e:
        print(f"Error occured while running snort_alert {e}")

def packetbeat():
    try:
        subprocess.Popen(["/home/doffy/packetbeat-8.13.4-linux-x86_64/packetbeat", "run", "--path.config", "/home/doffy/packetbeat-8.13.4-linux-x86_64"])
    except Exception as e:
        print(f"Error occured while running Packetbeat {e}")

def execute(choice):
   
    if choice == '1':
        Snort()
        u2json()
        snort_alert()
        print(f"Snort successfully running")
    elif choice == '2':
        packetbeat()
        print(f"Packetbeat successfully running")
    elif choice == '3':
        scan()
        print(f"initiating scan...")
    elif choice == '4':
        threat()
        print(f"Performing threat intelligence...")
    else:
        print(f"Unknown choice")
        return False
    return True

def main():
    print("###################################################################################################")
    print(f'''
1-IDS
2-Network monitor
3-Vulnerability scan
4-Threat intelligence
          ''')
    choices = input("Please select which options you would like to run\n")
    filebeat_activated = False
    for choice in choices.split():
        if not filebeat_activated:
            if choice in ['1','4','3']:
                filebeat()
                filebeat_activated=True
                print(f"Filebeat successfully running")
        success = execute(choice)
        if not success:
            print("Exiting")
            return
    while True:
        check = input("Run scan? (y/n)")
        if check == 'y':
            scan()

main()