from PySide6.QtCore import QTimer, QObject
from ui_weight import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class Alert():
    def __init__(self, widget):
        self.widget = widget
        self.initial_text = self.widget.text()
        self.initial_style = self.widget.styleSheet()

    def alert(self, message: str):
        self.widget.setText(message)
        # เพิ่มส่วนของคุณสมบัติ border-radius และเก็บค่า style ใหม่
        new_style = f"{self.initial_style} background-color: rgb(255, 17, 17); "
        self.widget.setStyleSheet(new_style)
        QTimer.singleShot(1500, lambda: self.widget.setText(self.initial_text))
        QTimer.singleShot(1500, lambda: self.widget.setStyleSheet(self.initial_style))

