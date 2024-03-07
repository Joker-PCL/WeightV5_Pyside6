from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize, Qt, QTimer, QUrl
from PySide6.QtGui import QPixmap, QIcon, QFont
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from src.Datetime import ShowDateTime
from src.Img import ShowImage
from src.Sound import PlaySound
from src.Thickness import Thickness
from weight import MySideBar

import sys
import os

# os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
profile = os.path.join(BASE_DIR, 'assets', 'images', 'scale.png')

def main():
    app = QApplication(sys.argv)
    
    with open("style.qss", "r") as file:
        _style = file.read()
        app.setStyleSheet(_style)
        
    # เลือกจอที่สอง
    screens = app.screens()
    second_screen = screens[1]  # ดัชนีที่ 1 หมายถึงจอที่สอง

    # สร้างหน้าต่างหลัก
    window = MySideBar()
    window.setWindowIcon(QIcon(profile))
    window.setWindowTitle("Weight 10s'")
    window.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowTitleHint | Qt.WindowStaysOnTopHint)
    window.setGeometry(second_screen.availableGeometry())  # ให้หน้าต่างเต็มจอ
    window.showFullScreen()
    
    thickness = Thickness(window)
    font = QFont()
    font.setPointSize(35)
    font.setBold(True)
    
    product_folder = os.path.join(BASE_DIR, 'product')
    test_img = ShowImage(window, product_folder)
    test_img.show_all()

    sounds_folder = os.path.join(BASE_DIR, 'sounds')
    file = 'sound1.mp3'
    test_sounds = PlaySound(sounds_folder)
    # test_sounds.play_all()

    printTime = ShowDateTime(window)
    printTime.show()
    window.button_exit_program.clicked.connect(test_sounds.stop)
        
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    
