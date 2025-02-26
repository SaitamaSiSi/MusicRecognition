import onnx

# Load a model
def main():
    # 修改onnx自定义元数据键值对
    model = onnx.load("F:/AIStudio/best.onnx")
    authorObj = model.metadata_props.add()
    authorObj.key = 'author'
    authorObj.value = 'RKO'
    versionObj = model.metadata_props.add()
    versionObj.key = 'version'
    versionObj.value = '0.0.1'
    liscenseObj = model.metadata_props.add()
    liscenseObj.key = 'license'
    liscenseObj.value = '© 2025, RKO Co., Ltd. All rights reserved.'
    descriptionObj = model.metadata_props.add()
    descriptionObj.key = 'description'
    descriptionObj.value = '模型描述'
    dateObj = model.metadata_props.add()
    dateObj.key = 'date'
    dateObj.value = '2025-01-23 09:21:00'
    onnx.save(model, 'F:/AIStudio/new_best.onnx')

if __name__ == '__main__':
    main()
