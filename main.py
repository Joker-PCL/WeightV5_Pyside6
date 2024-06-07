import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize, Qt, QTimer, QUrl
from PySide6.QtGui import QPixmap, QIcon, QFont
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from src.Datetime import ShowDateTime
from src.Img import ShowImage
from src.Sound import PlaySound
from src.WiFi import WiFi
from weight import Weight10s

##################################### ตั้งค่า ######################################
#################################################################################
OS_NAME = "Windows" # ตั้งค่าระบบปฏิบัติการ
BALANCE_PORT_WINDOWS = "COM6" # พอร์ต RS232 ** Windows("COM6")
BALANCE_PORT_LINUX = "/dev/ttyUSB0" # พอร์ต RS232 ** Linux("/dev/ttyUSB0")
#################################################################################
#################################################################################

if OS_NAME == "Windows":
    os.environ["QT_MEDIA_BACKEND"] = "windows"
    # os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"
    BALANCE_PORT = BALANCE_PORT_WINDOWS
elif OS_NAME == "Linux":
    os.environ["QT_MEDIA_BACKEND"] = "gstreamer"
    BALANCE_PORT = BALANCE_PORT_LINUX

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STYLE = os.path.join(BASE_DIR, "style.qss")
ICON = os.path.join(BASE_DIR, "assets", "images", "scale.png")

TOKEN = os.path.join(BASE_DIR, "files", "token.pickle")
CREDENTIALS = os.path.join(BASE_DIR, "files", "credentials.json")
SETTINGS = os.path.join(BASE_DIR, "files", "settings.json")

def main():
    app = QApplication(sys.argv)

    with open(STYLE, "r") as file:
        _style = file.read()
        app.setStyleSheet(_style)

    # เลือกจอที่สอง
    screens = app.screens()
    second_screen = screens[1]

    # สร้างหน้าต่างหลัก
    window = Weight10s(TOKEN, CREDENTIALS, SETTINGS, BALANCE_PORT)
    window.resize(1024, 600)
    window.move(0, 0)
    window.setWindowIcon(QIcon(ICON))
    window.setWindowTitle("Weight 10s'")
    window.setWindowFlags(
        Qt.FramelessWindowHint | Qt.WindowTitleHint | Qt.WindowStaysOnTopHint
    )
    window.setGeometry(second_screen.availableGeometry())  # ให้หน้าต่างเต็มจอ
    window.showFullScreen()
    # window.show()

    printTime = ShowDateTime(
        widget={"date_bar": window.date_bar, "time_bar": window.time_bar}
    )
    printTime.show()

    wifi = WiFi(window, os_name=OS_NAME)
    wifi.show_signal_icon()

    window.run()

    # product_folder = os.path.join(BASE_DIR, 'product')
    # test_img = ShowImage(window, product_folder)
    # test_img.show_all()

    sounds_folder = os.path.join(BASE_DIR, "sounds")
    # file = 'sound1.mp3'
    # test_sounds = PlaySound(sounds_folder)
    # test_sounds.play_all()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
