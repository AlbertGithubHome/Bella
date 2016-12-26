# send email test

from email.mime.text import MIMEText
import smtplib

#most simple email
'''
msg = MIMEText('这是一封来自神秘力量的谴责信，你竟然说XX不是王子，本文由脚本语言编写，由Albert通过后台自定义发送，你自己说，你是不是错了！', 'plain', 'utf-8')
msg['Subject'] = '神秘谴责信'
msg['From'] = 'xxx@163.com'
msg['To'] = 'yyy@qq.com'

print(msg)

# sender eamil
from_addr = input('From:')
password = input('Password:')

# receiver email
to_adrr = 'yyy@qq.com' #input('To:')

# smtp_server
smtp_server = 'smtp.163.com' #= input('SMTP server:')

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_adrr], msg.as_string())
server.quit()
'''

def send_text_mail(sender, password, receiver_list, subject = '', content = '', smtp_center= 'smtp.163.com'):

    # set message of needing to send
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ';'.join(receiver_list)

    # send email
    server = smtplib.SMTP(smtp_center, 25)
    server.set_debuglevel(1)
    server.login(sender, password)
    server.sendmail(sender, receiver_list, msg.as_string())
    server.quit()

def test_send_text_mail():

    from_addr = input('From:')
    password = input('Password:')
    to_adrr = '347070901@qq.com' #input('To:')

    subject = 'Python Email'
    content = 'This is a test email that created by python and sended by Albert!'

    # send email
    send_text_mail(from_addr, password, [to_adrr], subject, content)


if __name__ == '__main__':
    test_send_text_mail()