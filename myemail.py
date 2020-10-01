import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


# 보내는 사람 정보
me = "#개인 이메일 주소"
my_password = "#개인 이메일 비밀번호"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보
#여러사람에게 보낼 경우
emails = ['seongjin2710@naver.com']

for you in emails:

    you = "seongjin2710@naver.com"

    # 메일 기본 정보 설정
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "제목이다"
    msg['From'] = me
    msg['To'] = you

    # 메일 내용 쓰기
    content = "메일 내용이다"
    part2 = MIMEText(content, 'plain')
    msg.attach(part2)

#파일 첨부하는 기능
    part = MIMEBase('application', "octet-stream")
    with open("articles.xlsx", 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    #추석기사라는 제목으로 보내겠다
    part.add_header('Content-Disposition', "attachment", filename="썸네일을 포함한 기사 크롤링.xlsx")
    msg.attach(part)



    # 메일 보내고 서버 끄기
    s.sendmail(me, you, msg.as_string())
s.quit()