import  smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpserver='smtp.163.com'

user='xxxx@163.com'
password='....'

sender='xxxx@163.com'
receive='xxxx@qq.com'

subject='Web Selenium test report'
content='<html><h1 style="color:red">hello 51zxw </h1></html>'

msg=MIMEText(content,'html','utf-8')
# msg=MIMEText(content,'plain','utf-8') #纯文本邮件
msg['Subject']=Header(subject,'utf-8')
msg['From']='xxxx@163.com'
msg['To']='xxxx@qq.com'

smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

print("Start send Email...")
smtp.sendmail(sender,receive,msg.as_string())
smtp.quit()
print("Send Email end!")

