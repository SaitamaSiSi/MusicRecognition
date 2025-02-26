import pyotp
import sys

# 文件名
filename = 'secret_base.txt'
# 从文件中读取内容
with open(filename, 'r') as file:
    stored_sec = file.read()

# 假设这是您从文件中读取的密钥
totp = pyotp.TOTP(stored_sec)

# 获取当前时间戳下的OTP
current_otp = totp.now()

if len(sys.argv) > 1:
    scanned_otp = sys.argv[1]
    # 验证扫描得到的OTP
    if scanned_otp == current_otp:
        print("验证成功！")
    else:
        print("验证失败，请重试。")
