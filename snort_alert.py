

import yagmail
from time import sleep
PATH = "/var/log/snort/fast.log"
sender_addr = "SnortGP@gmail.com"
sender_password = "cohi xxtl gnll rkev"#app password



f = open(PATH,'r')
while True:
    
    line = f.readline()
    if line == "":
        sleep(5)
        continue
    prio = int(line.split(" ")[13][0])
    if prio <=2:

            yag = yagmail.SMTP(sender_addr, sender_password)
            subject = 'Snort Alert'
            body = line
            yag.send(

                to = receiver_email,
                subject= subject,
                contents=body

            )
    sleep(0.8)
        
