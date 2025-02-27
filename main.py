# 引入Flask库 pip install flask
import os
from flask import Flask

from librosaHelper import LibrosaHelper
from audioFluxHelper import AudioFluxHelper
from scikit_learn.scikitLearn import test as scikit_test1, test2 as scikit_test2

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


def run_api_test():
    app.run(host='0.0.0.0', port=5000)


def music_librosa_test():
    target_mp3 = os.path.join('music_check', "Test.mp3")

    # librosa库
    print('Librosa start')
    librosa_helper = LibrosaHelper('musicLibraryByLibrosa')
    librosa_helper.generate_music_library('music_library')
    librosa_helper.find_music(target_mp3)
    print('Librosa end')


def music_audioflux_test():
    target_mp3 = os.path.join('music_check', "Test.mp3")

    # audioflux库, 暂未实现
    print('Audioflux start')
    audioflux_helper = AudioFluxHelper('musicLibraryByAudioflux')
    audioflux_helper.generate_music_library('music_library')
    audioflux_helper.find_music(target_mp3)
    print('Audioflux end')


def scikit_learn_test():
    # scikit_test1()
    scikit_test2()


# 仅加入音频节奏比较，还需要MFCC、音频指纹等
if __name__ == '__main__':
    # run_api_test()
    # music_librosa_test()
    # music_audioflux_test()
    scikit_learn_test()

    print(f'Program Finished!')




