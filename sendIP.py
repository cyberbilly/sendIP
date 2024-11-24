import subprocess
import smtplib
#import socket
from email.mime.text import MIMEText
import datetime
from time import sleep
#account info
knownIP ="192.168.1.122"
sleep(15)
to = 'benots4@yahoo.com'
gmail_user = 'benots4@yahoo.com'
gmail_password = 'yuqymvgnavtgrayb'
smtpserver = smtplib.SMTP('smtp.mail.yahoo.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()
arg='ip route list'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data=p.communicate()
split_data=data[0].split()
ipaddr=split_data[split_data.index(b'src')+1].decode()
if str(ipaddr) not in knownIP:
    my_ip='Good day human overlord. This is your humble pi. My ip today is %r' % ipaddr
    msg=MIMEText(my_ip)
    msg['Subject']= 'Rpi2 Reporting in!'
    msg['From']= gmail_user
    msg['To'] = to
    smtpserver.sendmail(gmail_user, [to], msg.as_string())
    smtpserver.quit()
