import os
import sys
import threading
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget

# ตั้งค่า QT_MEDIA_BACKEND ให้เป็น windows
os.environ["QT_MEDIA_BACKEND"] = "windows"

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMediaPlayer Example")
        self.resize(800, 600)
        
        self.mediaPlayer = QMediaPlayer()
        self.videoWidget = QVideoWidget()
        self.audioOutput = QAudioOutput()
        self.audioOutput.setVolume(0)

        self.mediaPlayer.setAudioOutput(self.audioOutput)
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        
        layout = QVBoxLayout()
        layout.addWidget(self.videoWidget)
        centralWidget.setLayout(layout)
        
        self.mediaPlayer.setSource("SARAN.mp4")
        self.mediaPlayer.play()

app = QApplication(sys.argv)
player = VideoPlayer()
player.show()
sys.exit(app.exec())
