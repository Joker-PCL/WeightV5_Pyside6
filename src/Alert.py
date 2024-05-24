from PySide6.QtCore import QTimer

class Alert():
    def __init__(self, widget):
        self.widget = widget
        self.initial_text = self.widget.text()
        self.initial_style = self.widget.styleSheet()

    def alert(self, message: str = "", timeout: int = 1500):
        self.widget.setText(message)
        # เพิ่มส่วนของคุณสมบัติ border-radius และเก็บค่า style ใหม่
        new_style = f"{self.initial_style} background-color: rgb(255, 17, 17); "
        self.widget.setStyleSheet(new_style)
        QTimer.singleShot(timeout, lambda: self.widget.setText(self.initial_text))
        QTimer.singleShot(timeout, lambda: self.widget.setStyleSheet(self.initial_style))

    def alert_always(self, message: str = ""):
        self.widget.setText(message)
        # เพิ่มส่วนของคุณสมบัติ border-radius และเก็บค่า style ใหม่
        new_style = f"{self.initial_style} background-color: rgb(255, 17, 17); padding: 0px 20px; margin: 5px 0px"
        self.widget.setStyleSheet(new_style)

    def success(self, message: str = "", timeout: int = 1500, style: bool = True):
        self.widget.setText(message)
        # เพิ่มส่วนของคุณสมบัติ border-radius และเก็บค่า style ใหม่
        if style:
            new_style = f"{self.initial_style} background-color: rgb(0, 170, 127); "
            self.widget.setStyleSheet(new_style)
            
        QTimer.singleShot(timeout, lambda: self.widget.setText(self.initial_text))
        QTimer.singleShot(timeout, lambda: self.widget.setStyleSheet(self.initial_style))

    def loading(self, message: str = ""):
        self.widget.setText(message)

    def stop(self):
        self.widget.setText(self.initial_text)
        self.widget.setStyleSheet(self.initial_style)