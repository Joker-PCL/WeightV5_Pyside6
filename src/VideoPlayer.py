import sys
from PySide6.QtCore import QThread, Signal, Slot, QObject
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QApplication
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget

class VideoPlayer(QMainWindow):
    def __init__(self, widget: QWidget, fileName: str):
        super().__init__()
        
        self.media = QMediaPlayer()
        self.videoWidget = QVideoWidget()
        self.audioOutput = QAudioOutput()
        self.audioOutput.setVolume(1)
        
        self.media.setAudioOutput(self.audioOutput)
        self.media.setVideoOutput(self.videoWidget)
        
        layout = QVBoxLayout()
        layout.addWidget(self.videoWidget)
        widget.setLayout(layout)
        
        self.media.setSource(fileName)
        self.media.play()
        
