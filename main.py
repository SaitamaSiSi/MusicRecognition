# 引入Flask库 pip install flask
import os
from flask import Flask

from librosaHelper import LibrosaHelper
from audioFluxHelper import AudioFluxHelper

# 创建Flask应用实例
app = Flask(__name__)


# 定义一个路由，当访问根目录时返回"Hello, World!"
@app.route('/')
def hello_world():
    print_hi('PyCharm')
    return 'Hello, World!'


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 仅加入音频节奏比较，还需要MFCC、音频指纹等
if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)

    lib_name = 'musicLibrary'
    source_dir = 'music_library'
    target_mp3 = os.path.join('music_check', "Test.mp3")

    # librosa库
    print('Librosa start')
    librosa_lib_name = lib_name + 'ByLibrosa'
    librosaHelper = LibrosaHelper(librosa_lib_name)
    librosaHelper.generate_music_library(source_dir)
    librosaHelper.find_music(target_mp3)
    print('Librosa end')

    # audioflux库, 暂未实现
    # print('Audioflux start')
    # audioflux_lib_name = lib_name + 'ByAudioflux'
    # audiofluxHelper = AudioFluxHelper(audioflux_lib_name)
    # audiofluxHelper.generate_music_library(source_dir)
    # audiofluxHelper.find_music(target_mp3)
    # print('Audioflux end')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
