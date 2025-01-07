# pip install librosa numpy dtw
from numpy.linalg import norm
from numpy import array
from dtw import dtw
import librosa
import os
import numpy as np


class LibrosaHelper:

    def __init__(self, name):
        self.lib_name = name
        return

    def music_library_name(self):
        return self.lib_name + '.npy'

    def generate_music_library(self, source_dir):
        mp3_list = os.listdir(source_dir)
        music_library = {}
        for mp3 in mp3_list:
            mp3_name = os.path.join(source_dir, mp3)
            if mp3_name.endswith('.mp3'):
                # 音频数据y, 采样率sr
                audio_arr, sr = librosa.load(mp3_name)
                # 检测音频中的节拍事件, 并估计音频的节奏, 估计的全局节奏，单位是每分钟的拍数（BPM）tempo, 检测到的节拍事件的位置，这些位置以帧索引的形式表示music_frames
                tempo, music_frames = librosa.beat.beat_track(y=audio_arr, sr=sr)
                # 计算特征的增量, 得到节拍事件位置的变化率或动态变化特征
                music_frames = librosa.feature.delta(music_frames)
                music_library[mp3_name] = music_frames
        np.save(self.music_library_name(), music_library)

    def find_music(self, target_mp3):
        npy_file = np.load(self.music_library_name(), allow_pickle=True)
        music_library = npy_file.item()
        audio_arr, sr = librosa.load(target_mp3)
        tempo, music_frames = librosa.beat.beat_track(y=audio_arr, sr=sr)
        music_frames = librosa.feature.delta(music_frames)
        x = array(music_frames).reshape(-1, 1)

        compare_result = {}
        for songID in music_library.keys():
            song_frames = music_library[songID]
            y = array(song_frames).reshape(-1, 1)
            dist, cost, acc, path = dtw(x, y, dist=lambda x, y: norm(x - y, ord=1))
            print('Minimum distance found for ', songID.split("\\")[1], ": ", dist)
            compare_result[songID] = dist

        matched_song = min(compare_result, key=compare_result.get)

        print(matched_song)

# 参考 https://blog.csdn.net/wblgers1234/article/details/82499161
