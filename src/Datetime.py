from PySide6.QtCore import QTimer
from datetime import datetime
import random

class ShowDateTime():
    def __init__(self, window):
        self.date_bar = window.date_bar
        self.time_bar = window.time_bar

    def show(self):
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.print)
        self.timer.start() 
   
    def stop(self):
        self.timer.stop()
            
    def print(self):
        now = datetime.now() # current date and time
        curr_date = now.strftime("%d/%m/%Y")
        curr_time = now.strftime("%H:%M:%S")
        self.date_bar.setText(curr_date)
        self.time_bar.setText(curr_time)
        # self.rfid.setText(f"{random.randint(0, 9999999999):10d}")
        
