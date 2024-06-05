from PySide6.QtCore import QTimer
from datetime import datetime


class ShowDateTime():
    """ แสดงวันที่, เวลา """
    def __init__(self, widget: dict = {"date_bar", "time_bar"}):
        self.date_bar = widget["date_bar"]
        self.time_bar = widget["time_bar"]

    def show(self):
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.print)
        self.timer.start()

    def print(self):
        now = datetime.now()  # current date and time
        curr_date = now.strftime("%d/%m/%Y")
        curr_time = now.strftime("%H:%M:%S")
        self.date_bar.setText(curr_date)
        self.time_bar.setText(curr_time)
