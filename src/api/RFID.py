from PySide6.QtCore import QThread, Signal, Slot
from pynput import keyboard

class Rfid(QThread):
    # กำหนดสัญญาณที่จะส่งข้อมูลออกไป
    read = Signal(str)

    def __init__(self):
        super().__init__()
        self.rfid_text = ""

    def on_press(self, key):
        try:
            key_char = key.char
            if "1" <= key_char <= "9" or key_char == "0":
                self.rfid_text += key_char
        except Exception:
            pass

        if key == keyboard.Key.enter and self.rfid_text:
            return False  # หยุด listener เมื่อกดปุ่ม Enter

    @Slot(str)
    def run(self):
        self.rfid_text = ""
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
        self.read.emit(self.rfid_text)  # ส่งสัญญาณความคืบหน้า