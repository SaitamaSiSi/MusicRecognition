import json
import os
import math
import shutil

# 根据自己情况修改
# 源文件夹，小写jpg和json文件
filePath = "//datasets//val"
# 保存文件夹，保存jpg和txt文件
savePath = "//datasets//newVal"
# 空标注文件占比
emptyScale = 0.0
# 空标注文件初始数量
createEmptyCount = 0

def is_jpg_file(file_path):
    return file_path.lower().endswith('.jpg')

def copy_file(source_file, destination_file):
    shutil.copyfile(source_file, destination_file)

def convert_annotation(file, emptyCount):
    print('deal file => ', file)
    global createEmptyCount
    imgName = file.split(".")[0]
    jsonPath = filePath + '/' + imgName + '.json'
    txtPath = savePath + '/' + imgName + '.txt'
    oldJpgPath = filePath + '/' + file
    newJpgPath = savePath + '/' + file
    if not os.path.exists(jsonPath):
        if createEmptyCount < emptyCount:
            with open(txtPath, 'w') as noFile:
                createEmptyCount += 1
            copy_file(oldJpgPath, newJpgPath)
            print(jsonPath + '文件不存在，创建文件：' + txtPath)
    else:
        if os.path.getsize(jsonPath) == 0:
            return
        with open(jsonPath, 'r') as jsonFile:
            dict = json.load(jsonFile)
            imageWidth = dict.get('imageWidth')
            imageHeight = dict.get('imageHeight')
            shapes = dict.get('shapes')
            if any(shapes):
                if os.path.exists(txtPath):
                    os.remove(txtPath)
                for i in shapes:
                    label = i.get('label')
                    if label == 'person':
                        labelNum = 0
                    elif label == 'cat':
                        labelNum = 1
                    elif label == 'dog':
                        labelNum = 2
                    elif label == 'duck':
                        labelNum = 3
                    elif label == 'ball':
                        labelNum = 5
                    elif label == 'book':
                        labelNum = 7
                    points = i.get('points')
                    if len(points) != 4:
                        continue
                    pointLT = points[0]
                    pointRB = points[2]
                    centerX = round(((pointRB[0] - pointLT[0]) / 2 + pointLT[0]) / imageWidth, 6)
                    centerY = round(((pointRB[1] - pointLT[1]) / 2 + pointLT[1]) / imageHeight, 6)
                    boxW = round((pointRB[0] - pointLT[0]) / imageWidth, 6)
                    boxH = round((pointRB[1] - pointLT[1]) / imageHeight, 6)
                    with open(txtPath, 'a') as wFile:  # 写入txt文件中
                        print(labelNum, centerX, centerY, boxW, boxH, file=wFile)
                copy_file(oldJpgPath, newJpgPath)
                print('创建文件：' + txtPath)
            else:
                if (createEmptyCount < emptyCount):
                    with open(txtPath, 'w') as emptyFile:  # 写入txt文件中
                        createEmptyCount += 1
                    copy_file(oldJpgPath, newJpgPath)
                    print('标注点为空，创建文件：' + txtPath)

if __name__ == "__main__":
    fileList = os.listdir(filePath)
    jpgList = list(filter(lambda x: x.endswith('.jpg'), fileList))
    maxEmptyCount = math.floor(len(jpgList) * emptyScale)
    print(maxEmptyCount)
    for file in jpgList:
        if is_jpg_file(file):
            convert_annotation(file, maxEmptyCount)
