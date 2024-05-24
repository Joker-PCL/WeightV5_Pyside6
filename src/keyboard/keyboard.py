import sys
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQuick import QQuickView
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
keyboardStyle = os.path.join(BASE_DIR, "keyboard.qml")

def main():
    # Set the QT_IM_MODULE environment variable
    os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

    app = QGuiApplication(sys.argv)

    # Load QML file
    view = QQuickView()
    view.setSource(QUrl.fromLocalFile(keyboardStyle))

    # Show the keyboard
    view.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
