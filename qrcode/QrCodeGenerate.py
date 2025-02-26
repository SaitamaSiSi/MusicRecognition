import qrcode
import pyotp

# 文件名
filename = 'secret_base.txt'
# 从文件中读取内容
with open(filename, 'r') as file:
    stored_sec = file.read()
topt = pyotp.TOTP(stored_sec)
# 获取二维码 URI
qr_uri = topt.provisioning_uri('test')
# 生成二维码
img = qrcode.make(qr_uri)
# 保存或显示QR码图像
img.save("otp_qr.png")
#img.get_image().show() # 显示二维码
