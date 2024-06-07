from PySide6.QtCore import QTimer

class Alert():
    def __init__(self, widget):
        self.widget = widget
        self.initial_text = self.widget.text()
        self.initial_style = self.widget.styleSheet()

    def alert(self, message: str = "", timeout: int = 1500, style: bool = True):
        """
        เก็บค่า style ใหม่ \n
        message = ข้อความแจ้งเตือน \n
        timeout = เวลาในการแสดงข้อความแจ้งเตือน เริ่มต้น 1500 ms. \n
        style = เป็น bool เพื่อกำหนดว่าจะใช้ส่วนของคุณสมบัติ background-color, padding หรือไม่
        """

        self.widget.setText(message)
        # เพิ่มส่วนของคุณสมบัติ border-radius และเก็บค่า style ใหม่
        if style:
            new_style = f"{self.initial_style} background-color: rgb(255, 17, 17); padding: 0px 20px;"
            self.widget.setStyleSheet(new_style)
        else:
            self.widget.setStyleSheet(self.initial_style)

        QTimer.singleShot(timeout, lambda: self.widget.setText(self.initial_text))
        QTimer.singleShot(timeout, lambda: self.widget.setStyleSheet(self.initial_style))
        
    def alert_always(self, message: str = "", style: bool = True):
        """
        เก็บค่า style ใหม่ \n
        message = ข้อความแจ้งเตือน \n
        style = เป็น bool เพื่อกำหนดว่าจะใช้ส่วนของคุณสมบัติ background-color, padding หรือไม่
        """
                
        self.widget.setText(message)
        # เพิ่มส่วนของคุณสมบัติ border-radius และเก็บค่า style ใหม่
        if style:
            new_style = f"{self.initial_style} background-color: rgb(255, 17, 17); padding: 0px 20px;"
            self.widget.setStyleSheet(new_style)
        else:
            self.widget.setStyleSheet(self.initial_style)

    def success(self, message: str = "", timeout: int = 1500, style: bool = True):
        """
        เก็บค่า style ใหม่ \n
        message = ข้อความแจ้งเตือน \n
        timeout = เวลาในการแสดงข้อความแจ้งเตือน เริ่มต้น 1500 ms. \n
        style = เป็น bool เพื่อกำหนดว่าจะใช้ส่วนของคุณสมบัติ background-color, padding หรือไม่
        """

        self.widget.setText(message)
        # เพิ่มส่วนของคุณสมบัติ border-radius และเก็บค่า style ใหม่
        if style:
            new_style = f"{self.initial_style} background-color: rgb(0, 170, 127); padding: 0px 20px;"
            self.widget.setStyleSheet(new_style)
        else:
            self.widget.setStyleSheet(self.initial_style)
            
        QTimer.singleShot(timeout, lambda: self.widget.setText(self.initial_text))
        QTimer.singleShot(timeout, lambda: self.widget.setStyleSheet(self.initial_style))

    def loading(self, message: str = "", style: bool = True):
        """
        เก็บค่า style ใหม่ \n
        message = ข้อความแจ้งเตือน \n
        style = เป็น bool เพื่อกำหนดว่าจะใช้ส่วนของคุณสมบัติ background-color หรือไม่
        """

        self.widget.setText(message)
        if style:
            new_style = f"{self.initial_style} background-color: rgb(0, 170, 127);"
            self.widget.setStyleSheet(new_style)
        else:
            self.widget.setStyleSheet(self.initial_style)

    def stop(self):
        self.widget.setText(self.initial_text)
        self.widget.setStyleSheet(self.initial_style)