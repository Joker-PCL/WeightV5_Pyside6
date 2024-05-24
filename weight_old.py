from ui_weight import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QTimer
from PySide6.QtGui import QMovie
import os
from src.Alert import Alert
from src.api.File import File
from src.api.Server import Server

import serial
from pynput import keyboard
import threading

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GifFile = os.path.join(BASE_DIR, "assets", "gif", "connecting.gif")
PackingDataFile = os.path.join(BASE_DIR, "database", "PackingDataFile.json")
UserDataFile = os.path.join(BASE_DIR, "database", "userData.json")
SettingDataFile = os.path.join(BASE_DIR, "database", "setting10s.json")

MainSpreadsheetId = "1CP7r6TBxu_5HTqhE4mJ4-CPn_0XaxhET1pPp0WxTtRY"
UserDataRange = "User!A3:F"
SpreadsheetId = "1VecUHiEccSf7Z9TqO-ECSk_q0rDmXC2FT5TjSQL8GcY"
SettingRange = "Setting!B2:B17"

class Weight10s(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.current_page = self.home_page
        self.home_1.clicked.connect(lambda: self.switchToPage(self.current_page))
        self.home_2.clicked.connect(lambda: self.switchToPage(self.current_page))

        self.manual_1.clicked.connect(lambda: self.switchToPage(self.manual_page))
        self.manual_2.clicked.connect(lambda: self.switchToPage(self.manual_page))

        self.setting_1.clicked.connect(lambda: self.switchToPage(self.setting_page))
        self.setting_2.clicked.connect(lambda: self.switchToPage(self.setting_page))

        self.develops_1.clicked.connect(lambda: self.switchToPage(self.develops_page))
        self.develops_2.clicked.connect(lambda: self.switchToPage(self.develops_page))

        self.signout_1.clicked.connect(self.logout)
        self.signout_2.clicked.connect(self.logout)

        self.RFID_alert = Alert(self.rfid_alert)
        self.show_sidebar.setHidden(True)

        ##########################  characteristics ##########################
        self.characteristics_nomal.clicked.connect(lambda: self.characteristics("ปกติ"))
        self.characteristics_abnomal.clicked.connect(
            lambda: self.characteristics("ผิดปกติ")
        )

        ##########################  develops page   ##########################
        self.weight_page_view.clicked.connect(
            lambda: self.switchToPage(self.weighing_page)
        )
        self.thickness_page_view.clicked.connect(
            lambda: self.switchToPage(self.thickness_page)
        )
        self.characteristics_page_view.clicked.connect(
            lambda: self.switchToPage(self.characteristics_page)
        )
        self.summary_page_view.clicked.connect(
            lambda: self.switchToPage(self.summary_page)
        )
        self.summary_page_view.clicked.connect(
            lambda: self.switchToPage(self.summary_page)
        )
        self.button_exit_program.clicked.connect(
            lambda: self.switchToPage(self.process_page)
        )

        self.PackingDataFile = File(PackingDataFile)
        self.UserDataFile = File(UserDataFile)
        self.SettingDataFile = File(SettingDataFile)

        self.thickness_val = {}
        movie = QMovie(GifFile)
        self.process_img.setMovie(movie)
        movie.start()

    def switchToPage(self, page):
        self.stackedWidget.setCurrentWidget(page)

    def dbconnect(self, token, credentials):
        self.token = token
        self.credentials = credentials

        # สร้างอินสแตนซ์ของคลาส Server
        self.server = Server(token=self.token, credentials=self.credentials)

        # เรียกใช้เมธอด connect() เพื่อเชื่อมต่อ
        self.service = self.server.connect()
        self.updateDataUsers(MainSpreadsheetId, UserDataRange)
        self.updateSettingsData(SpreadsheetId, SettingRange)

    def updateDataUsers(self, spreadsheetId, range):
        def format_data(data):
            rfid = data[0]
            employeeId = data[1]
            usernameTH = data[2]
            usernameEN = data[3]
            role = data[5]

            return {
                "rfid": rfid,
                "employeeId": employeeId,
                "usernameTH": usernameTH,
                "usernameEN": usernameEN,
                "role": role,
            }

        dataUsers = self.server.getData(spreadsheetId, range)
        Lists = list(map(format_data, dataUsers))
        self.UserDataFile.write(Lists)

    def updateSettingsData(self, spreadsheetId, range):
        dataSettings = self.server.getData(spreadsheetId, range)
        settings = {
            "productName": dataSettings[0][0],  # ชื่อยา
            "lot": dataSettings[1][0],  # เลขที่ผลิต
            "balanceID": dataSettings[2][0],  # เครื่องชั่ง
            "tabletID": dataSettings[3][0],  # เครื่องตอก
            "meanWeight": dataSettings[4][0],  # น้ำหนักตามทฤษฎี
            "percentWeightVariation": dataSettings[5][0],  # เปอร์เซ็นเบี่ยงเบน
            "meanWeightMin": dataSettings[6][0],  # ช่วงน้ำหนัก 10 เม็ด(Min.)
            "meanWeightMax": dataSettings[7][0],  # ช่วงน้ำหนัก 10 เม็ด(Max.)
            "meanWeightRegMin": dataSettings[8][
                0
            ],  # ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ (Min.)
            "meanWeightRegMax": dataSettings[9][
                0
            ],  # ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ (Max.)
            "thicknessMin": dataSettings[10][0],  # ค่าความหนา(Min.)
            "thicknessMax": dataSettings[11][0],  # ค่าความหนา(Max.)
            "prepared": dataSettings[12][0],  # ตั้งค่าน้ำหนักโดย
            "approved": dataSettings[13][0],  # ตรวจสอบการตั้งค่าโดย
        }

        self.SettingDataFile.write(settings)

    def characteristics(self, selected):
        print(selected)

    ##########################  login page   ##########################
    def rfidCheckKey(self, key):
        try:
            key_char = key.char
            if "1" <= key_char <= "9" or key_char == "0":
                self.rfid_read += key_char
        except AttributeError:
            key_char = str(key)

        if key == keyboard.Key.enter:
            self.rfid_text += self.rfid_read
            self.rfid_read = ""

    def rfidListenForKeys(self):
        self.listener = keyboard.Listener(on_press=self.rfidCheckKey)
        self.listener.start()
        self.listener.join()  # รอจนกว่าจะเสร็จสิ้นหรือถูกยกเลิก

    def rfidScan(self):
        if self.rfid_text:
            self.rfid.setText(self.rfid_text)
            userData = self.rfidCheck(self.rfid_text)
            if userData:
                self.rfidStop()
                dataSettings = self.server.getData(
                    "1VecUHiEccSf7Z9TqO-ECSk_q0rDmXC2FT5TjSQL8GcY", "Setting!B2:B17"
                )
                productName = dataSettings[0][0]  # ชื่อยา
                lot = dataSettings[1][0]  # เลขที่ผลิต
                balanceID = dataSettings[2][0]  # เครื่องชั่ง
                tabletID = dataSettings[3][0]  # เครื่องตอก
                meanWeight = dataSettings[4][0]  # น้ำหนักตามทฤษฎี
                percentWeightVariation = dataSettings[5][0]  # เปอร์เซ็นเบี่ยงเบน
                meanWeightMin = dataSettings[6][0]  # ช่วงน้ำหนัก 10 เม็ด(Min.)
                meanWeightMax = dataSettings[7][0]  # ช่วงน้ำหนัก 10 เม็ด(Max.)
                meanWeightRegMin = dataSettings[8][0]  # ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ (Min.)
                meanWeightRegMax = dataSettings[9][0]  # ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ (Max.)
                thicknessMin = dataSettings[10][0]  # ค่าความหนา(Min.)
                thicknessMax = dataSettings[11][0]  # ค่าความหนา(Max.)
                prepared = dataSettings[12][0]  # ตั้งค่าน้ำหนักโดย
                approved = dataSettings[13][0]  # ตรวจสอบการตั้งค่าโดย
                finished = dataSettings[14][0]  # จบการผลิตโดย
                finishTime = dataSettings[15][0]  # จบการผลิตเวลา

                self.Productname.setText(productName)
                self.Lot.setText(lot)
                self.BalanceID.setText(balanceID)
                self.TabletID.setText(tabletID)
                self.Weight10s.setText(meanWeight + " กรัม")
                self.Weight10sPer.setText(percentWeightVariation)
                self.MeanWeightInhouse.setText(
                    meanWeightMin + " - " + meanWeightMax + " กรัม"
                )
                self.MeanWeightREG.setText(
                    meanWeightRegMin + " - " + meanWeightRegMax + " กรัม"
                )
                self.Thickness.setText(
                    thicknessMin + " - " + thicknessMax + " มิลลิเมตร(mm.)"
                )
                self.Operator.setText(userData["usernameTH"])

                self.current_page = self.weighing_page
                QTimer.singleShot(
                    1500,
                    lambda: self.switchToPage(self.current_page),
                )
                self.signout_1.setHidden(False)
                self.signout_2.setHidden(False)

            else:
                self.RFID_alert.alert("ไม่พบ RFID ของท่าน")
                self.rfid_text = ""

            QTimer.singleShot(1500, lambda: self.rfid.setText("XXXXXXXXXX"))

    def rfidCheck(self, rfid_text):
        userDataLists = self.UserDataFile.read()
        for index, data in enumerate(userDataLists):
            if data["rfid"] == rfid_text:
                return {"usernameTH": data["usernameTH"], "role": data["role"]}
        return None

    def rfidThreadStart(self):
        self.key_listener_thread = threading.Thread(target=self.rfidListenForKeys)
        self.key_listener_thread.start()

    def rfidStart(self):
        self.rfid_text = ""
        self.rfid_read = ""
        self.rfidThreadStart()
        self.rfidTimer = QTimer()
        self.rfidTimer.setInterval(5)
        self.rfidTimer.timeout.connect(self.rfidScan)
        self.rfidTimer.start()

    def rfidStop(self):
        if self.listener.running:
            self.rfidTimer.stop()
            self.rfidTimer.deleteLater()
            self.listener.stop()  # หยุดการทำงานของ listener
            self.listener.join()  # รอจนกว่า listener จะเสร็จสิ้นหรือถูกยกเลิก

    ##########################  weighing page   ##########################
    def readSerial(self):
        self.weighinData = []
        # อ่านค่าจาก port rs232
        # w = self.serial.readline()
        # currentWeight = str(random.uniform(0.155,0.165))

        while len(self.weighinData) < 2:
            w = input("Weight: ")
            currentWeight = w.decode('ascii', errors='ignore')
            currentWeight = currentWeight.replace("?", "").strip().upper()
            currentWeight = currentWeight.replace("G", "").strip()
            currentWeight = currentWeight.replace("N", "").strip()
            currentWeight = currentWeight.replace("S", "").strip()
            currentWeight = currentWeight.replace("T,", "").strip()  # AND FX
            currentWeight = currentWeight.replace("G", "").strip()  # AND FX
            currentWeight = currentWeight.replace("+", "").strip()
            weight = round(float(currentWeight), 3)

            self.weighinData["weight" + str(self.weighinData)] = weight

    def readSerialThreadStart(self):
        self.SerialThread = threading.Thread(target=self.readSerial)
        self.SerialThread.start()

    def readSerialThreadStop(self):
        if self.SerialThread.running:
            self.rfidTimer.stop()
            self.rfidTimer.deleteLater()
            self.SerialThread.stop()  # หยุดการทำงานของ listener
            self.SerialThread.join()  # รอจนกว่า listener จะเสร็จสิ้นหรือถูกยกเลิก

    def logout(self):
        self.current_page = self.process_page
        self.rfidStop()
        self.switchToPage(self.current_page)
        self.run()
        # QApplication.quit()

    def run(self):
        # self.serial = serial.Serial(port="/dev/ttyUSB0", baudrate=9600)
        self.current_page = self.process_page
        self.switchToPage(self.current_page)
        self.setting_1.setHidden(True)
        self.setting_2.setHidden(True)
        self.develops_1.setHidden(True)
        self.develops_2.setHidden(True)
        self.signout_1.setHidden(True)
        self.signout_2.setHidden(True)
        self.home_2.setChecked(True)

        self.current_page = self.home_page
        QTimer.singleShot(1500, lambda: self.switchToPage(self.current_page))

        self.rfidStart()
