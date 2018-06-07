import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpserver='smtp.163.com'

user='xxxx@163.com'
password='...'

sender='xxxx@163.com'
receives=['xxxx@126.com','xxxx@sina.com']

subject='Web Selenium Test report'
content='<html><h1 style="color:red">This is report  Content</h1></html>'

msg=MIMEText(content,'html','utf-8')
msg['Subject']=Header(subject,'utf-8')
msg['From']=sender
msg['To']=','.join(receives)

smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

print("Start send email...")
smtp.sendmail(sender,receives,msg.as_string())
smtp.quit()
print("Send email end!")