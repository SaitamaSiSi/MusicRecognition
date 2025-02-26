import os
import shutil

# 源文件夹
filePath = "//datasets/val"
# 保存文件夹
savePath = "//datasets/newVal"


def is_txt_file(file_path):
    return file_path.lower().endswith('.txt')

def copy_file(source_file, destination_file):
    shutil.copyfile(source_file, destination_file)

def convert_annotation(file):
    sourcePath = filePath + '/' + file
    targetPath = savePath + '/' + file
    # 读取txt文件内容
    with open(sourcePath, 'r') as file:
        lines = file.readlines()
        modified_lines = []
        for line in lines:
            newLine = list(line)
            # if newLine[0] == '2' or newLine[0] == '3' or newLine[0] == '4':
            #     newLine[0] = '1'
            # if newLine[0] == '5':
            #     newLine[0] = '2'
            if newLine[0] == '1':
                newLine[0] = '2'
            elif newLine[0] == '2':
                newLine[0] = '1'
            modified_lines.append(''.join(newLine))

        # 将修改后的内容写回txt文件
        with open(targetPath, 'w') as file:
            for line in modified_lines:
                file.write(line)

if __name__ == "__main__":
    fileList = os.listdir(filePath)
    txtList = list(filter(lambda x: x.endswith('.txt'), fileList))
    otherList = [item for item in fileList if item not in txtList]
    txtLen = len(txtList)
    othLen = len(otherList)
    index = 1
    for file in txtList:
        print(index, '/', txtLen, 'deal txt => ', file)
        index += 1
        if is_txt_file(file):
            convert_annotation(file)
    index = 1
    for oth in otherList:
        print(index, '/', othLen, 'deal img => ', oth)
        index += 1
        sourceP = filePath + '/' + oth
        targetP = savePath + '/' + oth
        copy_file(sourceP, targetP)


