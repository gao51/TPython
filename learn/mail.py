import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from learn.ler1 import mailWrite


def addimg(src, imgid):  # 文件路径、图片id
    fp = open(src, 'rb')  # 打开文件
    msgImage = MIMEImage(fp.read())  # 读入 msgImage 中
    fp.close()  # 关闭文件
    msgImage.add_header('Content-ID', imgid)
    return msgImage

msg_from = '279525177@qq.com'  # 发送方邮箱
passwd = 'utkkhhlkzlmhcacg'
msg_to = ['gaozh51@163.com' ]  # 收件人邮箱

subject = "python邮件测试"  # 主题
content = "这是我使用python smtplib及email模块发送的邮件"  # 正文
msg = MIMEMultipart('related')
mail = """<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>测试报告</title> 
</head>
<body>
  <table width="70%" border="1" cellspacing="1" cellpadding="4" bgcolor="#cccccc" class="tabtop13"align="center">
    <tr>
    <td colspan="20" class="btbg font-center titfont" rowspan="1" align="center">测试概况</td>
  </tr>
  <tr>
    <td width="8%" class="btbg font-center titfont" rowspan="4" > <img src="cid:logo",width="100%" height="100%"> </td>
    <td width="15%" class="btbg font-center titfont" rowspan="1"align="center">项目名称</td></td>
    <td width="15%" class="btbg font-center titfont" rowspan="1"align="center">FishSaying</td>
    <td width="15%" class="btbg font-center titfont" rowspan="1"align="center">用例总数</td>
    <td width="15%" class="btbg font-center titfont" rowspan="1"align="center">3</td>
    <td width="15%"class="btbg font-center titfont" rowspan="1"align="center">通过率</td>
  </tr>
  <tr>
    <td width="16%" class="btbg font-center titfont" rowspan="1"align="center">接口版本</td></td>
    <td width="16%" class="btbg font-center titfont" rowspan="1"align="center">——</td>
    <td width="16%" class="btbg font-center titfont" rowspan="1"align="center">通过总数</td>
    <td class="btbg font-center titfont"align="center">2</td>
    <td width="16%" class="btbg font-center titfont" rowspan="3"align="center">rate</td>
</tr>
<tr>
    <td width="10%" class="btbg font-center titfont" rowspan="1"align="center">脚本语言</td></td>
    <td width="10%" class="btbg font-center titfont" rowspan="1"align="center">python3.0</td>
    <td width="10%" class="btbg font-center titfont" rowspan="1"align="center">失败总数</td>
    <td  class="btbg font-center titfont"align="center">1</td>
      <tr>
    <td width="10%" class="btbg font-center titfont" rowspan="1"align="center">测试网络</td></td>
    <td width="10%" class="btbg font-center titfont" rowspan="1"align="center">——</td>
    <td width="10%" class="btbg font-center titfont" rowspan="1"align="center">测试日期</td>
    <td class="btbg font-center titfont"align="center">1</td>
</table>
</body>
</html>"""

msgtext = MIMEText(mail,"html","utf-8")
msg.attach(msgtext)

# mail = mail.replace("_img","G:\\code\\Tpython\\learn\\long.jpg")
# msg = MIMEText(mail, 'html', 'utf-8')
msg.attach(addimg("G:\\code\\Tpython\\learn\\Logo.png","logo"))
# msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = 'gaozh51@163.com'
try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print("发送成功")

except Exception as e:
    print(e)
finally:
    s.quit()
