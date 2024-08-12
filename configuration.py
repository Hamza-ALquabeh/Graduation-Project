def configure_filebeat(cloud_id, user, password):
    #add the users cloud.id and cloud.auth
    #add scan_results.txt input
    #add int_results.txt input
    #add the snort.json input    
    f = open("/home/doffy/filebeat-8.13.4-linux-x86_64/filebeat.yml","a")
    cloud_id = "f4edf60c28f647bb9049fd600de5fb55:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyQyMjk3MmVkZmUyZWM0MDNhODRmZTI4NDAyNDQ1MzRjOCQ1ZGExNWY2OWZkNGI0MjQyYmE3MTNjMjg1Mjk4YzYwNw=="
    user = "filebeat"
    password = "hamzamohd"

    config = f'''
    
cloud.id: "{cloud_id}"

cloud.auth: "{user}:{password}"

'''
    f.write(f"{config}\n")
    f.close()


def configure_packetbeat(cloud_id, user, password):
    #add the users cloud.id and cloud.auth
    f = open("/home/doffy/packetbeat-8.13.4-linux-x86_64/packetbeat.yml","a")
    cloud_id = "f4edf60c28f647bb9049fd600de5fb55:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyQyMjk3MmVkZmUyZWM0MDNhODRmZTI4NDAyNDQ1MzRjOCQ1ZGExNWY2OWZkNGI0MjQyYmE3MTNjMjg1Mjk4YzYwNw=="
    user = "packetbeat"
    password = "hamzamohd"
    config = f'''
       
cloud.id: "{cloud_id}"

cloud.auth: "{user}:{password}"

'''
    f.write(f"{config}\n")
    f.close()

def configure_snort_and_scan(home_ip):
    #set the home network variable
    #set the unified2 output file
    #set the fast alert file
    #set the network variable in the scan script
    f = open("/etc/snort/snort.conf","a")
    config = f'''
    
ipvar HOME_NET {home_ip}
output alert_fast: fast.log
    
    '''
    f.write(f"{config}\n")
    f.close

    f = open("/home/doffy/Desktop/GP/nmap_scan.py",'r')
    temp = f.read()
    f.close()
    f = open("/home/doffy/Desktop/GP/nmap_scan.py",'w')
    f.write(f"TARGET_SUBNET = '{home_ip}'\n")
    f.write(temp)
    f.close()

def configure_alert(email_addr):
    #add the given email address to the alert script
    f = open(f"/home/doffy/Desktop/GP/snort_alert.py","r")
    temp = f.read()
    f.close()
    f = open("/home/doffy/Desktop/GP/snort_alert.py", 'w')
    f.write(f"receiver_email = '{email_addr}'\n")    
    f.write(temp)
    f.close()

def main():
    try:
        print(f"................................Configuration..................................")
        print("################################################################################")
        
        print("---------Filebeat configuration---------")
        cloud = input("Please Enter your cloud ID\n")
        user  = input("Please Enter your user\n")
        password = input("Please Enter your password\n")
        configure_filebeat(cloud, user, password)
        print("################################################################################")
        
        print("---------Packetbeat configuration---------")
        cloud = input("Please Enter your cloud ID\n")
        user  = input("Please Enter your user\n")
        password = input("Please Enter your password\n")
        configure_packetbeat(cloud, user, password)
        print("################################################################################")
        
        print("---------Snort configuration---------")
        ip = input("Please enter your home network in the same format as 192.168.1.0/24\n")
        configure_snort_and_scan(ip)
        print("################################################################################")
        
        print("---------alerts configuration---------")
        email = input("Please enter the E-mail address you want to receive alerts on\n")
        configure_alert(email)
        
        print(f"Configuration complete\n")
    
    except Exception as e:
        print(f"Error occured {e}")
        print(f"Exiting...")    

main()