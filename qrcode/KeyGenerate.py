import pyotp

sec = pyotp.random_base32()
# 文件名
filename = 'secret_base.txt'
# 将安全令牌基础写入文件
with open(filename, 'w') as file:
    file.write(sec)
print(f"安全令牌基础已保存到文件 {filename}")