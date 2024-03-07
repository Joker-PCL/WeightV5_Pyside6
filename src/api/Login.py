from PySide6.QtCore import QTimer, QCoreApplication
from PySide6.QtWidgets import QApplication
from pynput import keyboard
import threading

class Login():
    def __init__(self, widget, alert):
        self.widget = widget
        self.alert = alert
        self.rfid_read = ""
        self.rfid = ""
        self.listener = None
        self.scaner_flag = False
        
        self.initial_text = self.widget.text()

    def on_press(self, key):
        try:
            key_char = key.char
            if '1' <= key_char <= '9' or key_char == '0':
                self.rfid_read += key_char
        except AttributeError:
            key_char = str(key)
        
        if key == keyboard.Key.enter:
            self.rfid += self.rfid_read 
            self.rfid_read = ""
        
        # ตั้งค่า flag สำหรับหยุดการทำงาน
        if key == keyboard.Key.enter:
            self.scaner_flag = True

    def listen_for_keys(self): 
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        self.listener.join()  # รอจนกว่าจะเสร็จสิ้นหรือถูกยกเลิก

    def scan(self):
        self.thread_start()
        self.timer = QTimer()
        self.timer.setInterval(5)
        self.timer.timeout.connect(self.rfid_scan)
        self.timer.start() 
        
    def rfid_scan(self):
        if self.rfid:
            self.widget.setText(self.rfid)
            self.rfid_check(self.rfid)
            QTimer.singleShot(1500, lambda: self.widget.setText(self.initial_text))
            print("text: ", self.rfid)
            self.rfid = ""
            
    def rfid_check(self, rfid):
        if rfid == "1514075799":
            self.stop()
        else:
            self.alert.alert("ไม่พบ RFID ของท่าน")
        
    def thread_start(self):
        self.key_listener_thread = threading.Thread(target=self.listen_for_keys)
        self.key_listener_thread.start()

    def stop(self):
        if self.listener.running:
            self.timer.stop()
            self.timer.deleteLater()
            self.listener.stop()  # หยุดการทำงานของ listener
            self.listener.join()  # รอจนกว่า listener จะเสร็จสิ้นหรือถูกยกเลิก

