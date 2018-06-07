import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtpserver='smtp.163.com'

user='xxxx@163.com'
password='...'

sender='xxxx@163.com'
receives=['xxxx@126.com','xxxx@sina.com']

subject='Web Selenium Test report'
content='<html><h1 style="color:red">This is report  Content</h1></html>'

send_file=open(r'E:\Python_script\logo.png','rb').read()

att=MIMEText(send_file,'base64','utf-8')
att['Content-Type']='application/octet-stream'
att['Content-Disposition']='attachment;filename="logo.png"'


msgRoot=MIMEMultipart()
msgRoot.attach(MIMEText(content,'html','utf-8'))
msgRoot['Subject']=subject
msgRoot['From']=sender
msgRoot['To']=','.join(receives)
msgRoot.attach(att)

smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

print("Start send email...")
smtp.sendmail(sender,receives,msgRoot.as_string())
smtp.quit()
print("Send email end!")



