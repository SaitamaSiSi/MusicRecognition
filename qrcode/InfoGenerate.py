import qrcode

# 设备基础信息
device_info = {
    "name": "ZYH_NAS_Z4PRO",
    "serial_number": "SN42108991",
    "location": "重庆市南岸区十一中",
    "status": "离线"
}

# 将设备信息转换为JSON字符串
device_info_str = str(device_info)

# 创建二维码对象
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# 添加数据到二维码
qr.add_data(device_info_str)
qr.make(fit=True)

# 创建二维码图片
img = qr.make_image(fill='black', back_color='white')

# 保存二维码图片
img.save("device_qr_code.png")