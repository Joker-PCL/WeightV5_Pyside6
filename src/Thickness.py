from PySide6.QtCore import QThread, Signal, Slot
from src.Alert import Alert

class Thickness(QThread):
    get = Signal(dict)

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.current_value = ""
        self.max_range = 5 # max range
        self.current_number = None # current thickness widget number
        self.thicknessData = {} # thickness values
        
        ##########################   Keyboard   ##########################
        self.window.key_1.clicked.connect(lambda: self.read_key("1"))
        self.window.key_2.clicked.connect(lambda: self.read_key("2"))
        self.window.key_3.clicked.connect(lambda: self.read_key("3"))
        self.window.key_4.clicked.connect(lambda: self.read_key("4"))
        self.window.key_5.clicked.connect(lambda: self.read_key("5"))
        self.window.key_6.clicked.connect(lambda: self.read_key("6"))
        self.window.key_7.clicked.connect(lambda: self.read_key("7"))
        self.window.key_8.clicked.connect(lambda: self.read_key("8"))
        self.window.key_9.clicked.connect(lambda: self.read_key("9"))
        self.window.key_0.clicked.connect(lambda: self.read_key("0"))
        self.window.key_dot.clicked.connect(lambda: self.read_key("."))
        self.window.key_backspace.clicked.connect(lambda: self.read_key("backspace"))
        self.window.key_enter.clicked.connect(lambda: self.read_key("enter"))
        self.window.key_cancel.clicked.connect(lambda: self.read_key("cancel"))
        
        ##########################   thickness   ##########################
        self.thickness_keyboard = self.window.thickness_keyboard
        self.thickness_alert = Alert(self.window.thickness_title)
        self.thickness_alert_input = Alert(self.window.thickness_input_title)
        self.thickness_val_label = self.window.thickness_val_label

        self.initial_text = self.window.thickness_val_1.text()
        self.initial_style = self.window.thickness_val_1.styleSheet()
        self.window.thickness_val_1.clicked.connect(lambda: self.thickness_input(self.window.thickness_val_1))
        self.window.thickness_val_2.clicked.connect(lambda: self.thickness_input(self.window.thickness_val_2))
        self.window.thickness_val_3.clicked.connect(lambda: self.thickness_input(self.window.thickness_val_3))
        self.window.thickness_val_4.clicked.connect(lambda: self.thickness_input(self.window.thickness_val_4))
        self.window.thickness_val_5.clicked.connect(lambda: self.thickness_input(self.window.thickness_val_5))
        self.window.thickness_val_6.clicked.connect(lambda: self.thickness_input(self.window.thickness_val_6))
        self.window.thickness_val_7.clicked.connect(lambda: self.thickness_input(self.window.thickness_val_7))
        self.window.thickness_val_8.clicked.connect(lambda: self.thickness_input(self.window.thickness_val_8))
        self.window.thickness_val_9.clicked.connect(lambda: self.thickness_input(self.window.thickness_val_9))
        self.window.thickness_val_10.clicked.connect(lambda: self.thickness_input(self.window.thickness_val_10))
        
        self.window.button_thickness_confirm.clicked.connect(lambda: self.thickness(True))
        self.window.button_thickness_cancel.clicked.connect(lambda: self.thickness(False))
        
    # Event ปุ่ม ยืนยัน และ ยกเลิก
    @Slot(dict)
    def thickness(self, selected):
        # ป้อนข้อมูลความหนา
        if selected:   
            thickness_check = True

            # เช็คข้อมูลความหนาครบ 10 เม็ด
            for i in range(1, 11):
                thickness = getattr(self.window, f"thickness_val_{i}")
                
                if thickness.text() == "XX.XX":
                    thickness_check = False
                    break 
                else:
                    # เพิ่มข้อมูลความหนาลงใน dictionary
                    self.thicknessData[f"number_{i}"] = thickness.text()
                    
            if thickness_check:
                self.get.emit(self.thicknessData)
            else:
                self.thickness_alert.alert("กรุณากรอกข้อมูลให้ครบ")
            
        # ไม่ป้อนข้อมูลความหนา 
        else:
            for i in range(1, 11):
                self.thicknessData[f"number_{i}"] = "-"
                thickness_number = getattr(self.window, f"thickness_val_{i}")
                thickness_number.setText(self.initial_text)
                thickness_number.setStyleSheet(self.initial_style)

            self.get.emit(self.thicknessData)

    # ป้อนข้อมูลความหนา
    def thickness_input(self, thickness_number):
        self.current_number = thickness_number
        number = thickness_number.objectName()
        thickness_number_value = thickness_number.text()
        
        self.thickness_val_label.setText(f"เม็ดที่ {number.replace('thickness_val_', '')}")
        self.window.switchToPage(self.window.thickness_keyboard)
        
        if thickness_number_value != "XX.XX":
            self.current_value = thickness_number_value
            self.window.thickness_val_input.setText(thickness_number_value)
           
    # อ่านข้อมูลจาก widgets keyboard 
    def read_key(self, key: str):
        if key == "enter":
            value = self.current_value
            if len(value):
                try:
                    self.current_number.setText(f"{float(value):.2f}")
                    self.thicknessOutoffRange(float(value))
                    self.window.switchToPage(self.window.thickness_page)
                    self.current_value = ""
                    self.window.thickness_val_input.setText("XX.XX")
                except ValueError:
                    self.thickness_alert_input.alert("ข้อมูลไม่ถูกต้อง")
            else:
                self.thickness_alert_input.alert("กรุณากรอกข้อมูลให้ครบ")
        elif key == "cancel":
            self.window.switchToPage(self.window.thickness_page)
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

    def thicknessOutoffRange(self, thickness):
        widget = self.current_number
        initial_text = widget.text()
        initial_style = widget.styleSheet()
        inRange_style = f"{initial_style} color: rgb(0, 170, 127);"
        outOffRange_style = f"{initial_style} color: rgb(255, 17, 17);"

        if thickness <= 1:
            widget.setStyleSheet(inRange_style)
        else:
            widget.setStyleSheet(outOffRange_style)