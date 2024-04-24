from PySide6.QtWidgets import QApplication
from src.Alert import Alert

class Thickness():
    def __init__(self, window):
        self.window = window
        self.current_value = ""
        self.max_range = 5 # max range
        self.current_number = None # current thickness widget number
        self._thickness_val = {} # thickness values
        
        ##########################   Keyboard   ##########################
        window.key_1.clicked.connect(lambda: self.read_key("1"))
        window.key_2.clicked.connect(lambda: self.read_key("2"))
        window.key_3.clicked.connect(lambda: self.read_key("3"))
        window.key_4.clicked.connect(lambda: self.read_key("4"))
        window.key_5.clicked.connect(lambda: self.read_key("5"))
        window.key_6.clicked.connect(lambda: self.read_key("6"))
        window.key_7.clicked.connect(lambda: self.read_key("7"))
        window.key_8.clicked.connect(lambda: self.read_key("8"))
        window.key_9.clicked.connect(lambda: self.read_key("9"))
        window.key_0.clicked.connect(lambda: self.read_key("0"))
        window.key_dot.clicked.connect(lambda: self.read_key("."))
        window.key_backspace.clicked.connect(lambda: self.read_key("backspace"))
        window.key_enter.clicked.connect(lambda: self.read_key("enter"))
        window.key_cancel.clicked.connect(lambda: self.read_key("cancel"))
        
        ##########################   thickness   ##########################
        self.thickness_keyboard = self.window.thickness_keyboard
        self.thickness_alert = Alert(window.thickness_title)
        self.thickness_alert_input = Alert(window.thickness_input_title)
        self.thickness_val_label = window.thickness_val_label
    
        window.thickness_val_1.clicked.connect(lambda: self.thickness_input(window.thickness_val_1))
        window.thickness_val_2.clicked.connect(lambda: self.thickness_input(window.thickness_val_2))
        window.thickness_val_3.clicked.connect(lambda: self.thickness_input(window.thickness_val_3))
        window.thickness_val_4.clicked.connect(lambda: self.thickness_input(window.thickness_val_4))
        window.thickness_val_5.clicked.connect(lambda: self.thickness_input(window.thickness_val_5))
        window.thickness_val_6.clicked.connect(lambda: self.thickness_input(window.thickness_val_6))
        window.thickness_val_7.clicked.connect(lambda: self.thickness_input(window.thickness_val_7))
        window.thickness_val_8.clicked.connect(lambda: self.thickness_input(window.thickness_val_8))
        window.thickness_val_9.clicked.connect(lambda: self.thickness_input(window.thickness_val_9))
        window.thickness_val_10.clicked.connect(lambda: self.thickness_input(window.thickness_val_10))
        
        window.button_thickness_confirm.clicked.connect(lambda: self.thickness(True))
        window.button_thickness_cancel.clicked.connect(lambda: self.thickness(False))
    
    # Event ปุ่ม ยืนยัน และ ยกเลิก
    def thickness(self, selected):
        # ป้อนข้อมูลความหนา
        if selected:   
            thickness_check = True
            thickness_data = {}  # สร้าง dictionary เพื่อเก็บข้อมูลความหนา

            # เช็คข้อมูลความหนาครบ 10 เม็ด
            for i in range(1, 11):
                thickness = getattr(self.window, f"thickness_val_{i}")
                
                if thickness.text() != "XX.XX":
                    thickness_check = False
                    break 
                else:
                    # เพิ่มข้อมูลความหนาลงใน dictionary
                    thickness_data[f"number_{i}"] = thickness.text()
                    
            if thickness_check:
                thickness_obj = {"thickness": thickness_data}  # สร้างโครงสร้าง JSON
                self.window.packing_data.append(thickness_obj)
            else:
                self.thickness_alert.alert("กรุณากรอกข้อมูลให้ครบ")
            
        # ไม่ป้อนข้อมูลความหนา 
        else:
            for i in range(1, 11):
                self._thickness_val[f"thickness_val_{i}"] = "-"
                thickness_number = getattr(self.window, f"thickness_val_{i}")
                thickness_number.setText("XX.XX")

    # ป้อนข้อมูลความหนา
    def thickness_input(self, thickness_number):
        self.current_number = thickness_number
        number = thickness_number.objectName()
        thickness_number_value = thickness_number.text()
        
        self.thickness_val_label.setText(f"เม็ดที่ {number.replace('thickness_val_', '')}")
        self.window.switch_to_Page(self.thickness_keyboard)
        
        if thickness_number_value != "XX.XX":
            self.current_value = thickness_number_value
            self.window.thickness_val_input.setText(thickness_number_value)
        
    # อ่านข้อมูลความหนาแล้วส่งค่ากลับ 
    def read(self):
        while True:
            if self._thickness_val:
                return self._thickness_val
            else:
                QApplication.processEvents()
    
    # อ่านข้อมูลจาก widgets keyboard 
    def read_key(self, key: str):
        if key == "enter":
            value = self.current_value
            if len(value):
                try:
                    self.current_number.setText(f"{float(value):.2f}")
                    self.window.switch_to_Page(self.window.thickness_page)
                    self.current_value = ""
                    self.window.thickness_val_input.setText("XX.XX")
                except ValueError:
                    self.thickness_alert_input.alert("ข้อมูลไม่ถูกต้อง")
            else:
                self.thickness_alert_input.alert("กรุณากรอกข้อมูลให้ครบ")
        elif key == "cancel":
            self.window.switch_to_Page(self.window.thickness_page)
            self.current_value = ""
            self.window.thickness_val_input.setText("XX.XX")
        elif key == "backspace":
            if len(self.current_value) > 0:
                self.current_value = self.current_value[:-1]
                self.window.thickness_val_input.setText(self.current_value)
                if len(self.current_value) == 0:
                    self.window.thickness_val_input.setText("XX.XX")        
        else:
            if len(self.current_value) < self.max_range:
                self.current_value += key
                self.window.thickness_val_input.setText(self.current_value)
                    