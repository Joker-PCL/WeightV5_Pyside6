from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize, Qt, QTimer, QUrl
from PySide6.QtGui import QPixmap, QIcon, QFont
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from src.Datetime import ShowDateTime
from src.Img import ShowImage
from src.Sound import PlaySound
from src.WiFi import WiFi
from weight import Weight10s

import sys
import os

os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
icon = os.path.join(BASE_DIR, "assets", "images", "scale.png")

token = os.path.join(BASE_DIR, "files", "token.pickle")
credentials = os.path.join(BASE_DIR, "files", "credentials.json")
settings = os.path.join(BASE_DIR, "files", "settings.json")

MainSpreadsheetId = "1CP7r6TBxu_5HTqhE4mJ4-CPn_0XaxhET1pPp0WxTtRY"
UserDataRange = "User!A3:F"
SpreadsheetId = "1VecUHiEccSf7Z9TqO-ECSk_q0rDmXC2FT5TjSQL8GcY"
SettingRange = "Setting!B2:B17"


def main():
    app = QApplication(sys.argv)

    with open("style.qss", "r") as file:
        _style = file.read()
        app.setStyleSheet(_style)

    # เลือกจอที่สอง
    screens = app.screens()
    second_screen = screens[0]

    # สร้างหน้าต่างหลัก
    window = Weight10s(
        token,
        credentials,
        settings
    )

    window.setWindowIcon(QIcon(icon))
    window.setWindowTitle("Weight 10s'")
    # window.setWindowFlags(
    #     Qt.FramelessWindowHint | Qt.WindowTitleHint | Qt.WindowStaysOnTopHint
    # )
    # window.setGeometry(second_screen.availableGeometry())  # ให้หน้าต่างเต็มจอ
    # window.showFullScreen()
    window.show()

    printTime = ShowDateTime(
        widget={"date_bar": window.date_bar, "time_bar": window.time_bar}
    )
    printTime.show()

    wifi = WiFi(window, os_name="Windows")
    wifi.show_signal_icon()

    window.run()

    # product_folder = os.path.join(BASE_DIR, 'product')
    # test_img = ShowImage(window, product_folder)
    # test_img.show_all()

    # sounds_folder = os.path.join(BASE_DIR, 'sounds')
    # file = 'sound1.mp3'
    # test_sounds = PlaySound(sounds_folder)
    # # test_sounds.play_all()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
