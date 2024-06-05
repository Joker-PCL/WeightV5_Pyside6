from PySide6.QtCore import QTimer, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
import os
# from playsound import playsound

class PlaySound():
    def __init__(self, path):
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.audio_output.setVolume(1)
        self.path = path
        self.sounds_files = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]
        self.sound_index = 0
        
    def play_all(self):
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.play_all)
        self.timer.start()
          
        if self.sounds_files and not self.player.isPlaying():
            _file = self.sounds_files[self.sound_index]
            print("Sound is playing: ", _file)
            self.play(_file)
            self.sound_index += 1
                
        if self.sound_index == len(self.sounds_files) - 1:
            self.sound_index = 0
            
    def play(self, file):
        if file and not self.player.isPlaying():
            _file = os.path.join(self.path, file)
            self.audio_output.setVolume(100)
            self.player.setAudioOutput(self.audio_output)
            self.player.setSource(QUrl.fromLocalFile(_file))
            self.player.play()
        
    def stop(self):
        if self.player.isPlaying():
            self.player.stop()
            self.timer.stop()
            self.timer.deleteLater()