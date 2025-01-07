# pip install audioflux
from audioflux.type import SpectralFilterBankScaleType, SpectralDataType
from numpy import array
from dtw import dtw
from numpy.linalg import norm
import os
import numpy as np
import audioflux as af


class AudioFluxHelper:
    def __init__(self, name):
        self.lib_name = name
        return

    def music_library_name(self):
        return self.lib_name + '.npy'

    def generate_music_library(self, source_dir):
        return
        mp3_list = os.listdir(source_dir)
        music_library = {}
        for mp3 in mp3_list:
            mp3_name = os.path.join(source_dir, mp3)
            if mp3_name.endswith('.mp3'):
                # 读取音频文件
                audio_arr, sr = af.read(mp3_name)
                music_frames = 'TODO'
                music_library[mp3_name] = music_frames
        np.save(self.music_library_name(), music_library)

    def find_music(self, target_mp3):
        return
        npy_file = np.load(self.music_library_name(), allow_pickle=True)
        music_library = npy_file.item()
        # 读取音频文件
        audio_arr, sr = af.read(target_mp3)

        compare_result = {}
        for songID in music_library.keys():
            song_frames = music_library[songID]

        matched_song = min(compare_result, key=compare_result.get)

        print(matched_song)
