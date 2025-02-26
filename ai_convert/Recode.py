import json
import os

# 源文件夹
filePath = "/datasets/dataSets01/Train"
# 保存文件夹
savePath = "/datasets/dataSets01//NewTrain"

def is_jpg_file(file_path):
    return file_path.lower().endswith('.txt')

def copy_file(source_file, destination_file):
    shutil.copyfile(source_file, destination_file)

def convert_annotation(file):
    jsonPath = filePath + '/' + file
    txtPath = savePath + '/' + file
    # 读取txt文件内容
    with open(jsonPath, 'r') as file:
        lines = file.readlines()
        modified_lines = []
        for line in lines:
            newLine = list(line)
            if newLine[0] != '1' or newLine[0] != '0':
                newLine[0] = '1'
            modified_lines.append(''.join(newLine))

        # 将修改后的内容写回txt文件
        with open(txtPath, 'w') as file:
            for line in modified_lines:
                file.write(line)

if __name__ == "__main__":
    fileList = os.listdir(filePath)
    jpgList = list(filter(lambda x: x.endswith('.txt'), fileList))
    for file in jpgList:
        if is_jpg_file(file):
            convert_annotation(file)


"""
import os
from PIL import Image

for image in os.listdir("F:/AIStudio/数据源/Source"):
    fake_img = Image.open('{}{}'.format("F:/AIStudio/数据源/Source/", image))
    if fake_img.mode != 'RGB':
        print('触发!')
        fake_img = fake_img.convert('RGB')
    ext = os.path.splitext(image)
    fake_img.save('{}{}.jpg'.format("F:/TestProgram/Test/AIStudio/数据源/Save/", ext[0]))
"""

"""
from PIL import Image
import paddle.vision.transforms as T

targetWidth = 224
targetHeight = 224
fake_img = Image.open("F:/AIStudio/数据源/test.png")
if fake_img.mode != 'RGB':
    fake_img = fake_img.convert('RGB')
fake_img.save("F:/TestProgram/Test/1.jpg")
newImage = Image.new('RGB',(targetHeight,targetWidth),(255,255,255))
if (fake_img.height, fake_img.width) != (targetHeight, targetWidth):
    xRatio = targetWidth / fake_img.width
    yRatio = targetHeight / fake_img.height
    ratio = min(xRatio, yRatio)
    width = int(fake_img.width * ratio)
    height = int(fake_img.height * ratio)
    x = (targetWidth / 2) - (width / 2)
    y = (targetHeight / 2) - (height / 2)
    newImageBox = (int(x), int(y), int(width + x), int(height + y))
    print(newImageBox)
    loadTransform = T.Resize(size=(height, width), interpolation='bicubic')
    loadImage = loadTransform(fake_img)
    print(loadImage.size)
    newImage.paste(loadImage, newImageBox, mask=None)
    newImage.save("F:/TestProgram/Test/2.jpg")
"""