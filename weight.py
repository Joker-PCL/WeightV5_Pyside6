import os
from ui_weight import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGroupBox, QVBoxLayout
from PySide6.QtCore import QCoreApplication, QTimer, Signal, Slot, QTimer, Qt, QSize
from PySide6.QtGui import QMovie, QFont, QCursor, QIcon
from datetime import datetime

from src.Alert import Alert
from src.api.File import File
from src.api.Server import Server
from src.api.RFID import Rfid
from src.Weighing import Weighing
from src.Thickness import Thickness
from src.TabletList import TabletList

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GifFile = os.path.join(BASE_DIR, "assets", "gif", "connecting.gif")
OfflineDataFile = os.path.join(BASE_DIR, "database", "offline.json")
PackingDataFile = os.path.join(BASE_DIR, "database", "packingData.json")
UserDataFile = os.path.join(BASE_DIR, "database", "usersData.json")
SettingDataFile = os.path.join(BASE_DIR, "database", "settings10s.json")


class Weight10s(QMainWindow, Ui_MainWindow):
    def __init__(
        self,
        token,
        credentials,
        settings
    ):
        super().__init__()

        self.token = token
        self.credentials = credentials
        self.settings = settings

        self.setupUi(self)
        self.current_page = self.home_page
        self.home_1.clicked.connect(lambda: self.switchToPage(self.current_page))
        self.home_2.clicked.connect(lambda: self.switchToPage(self.current_page))

        self.manual_1.clicked.connect(lambda: self.switchToPage(self.manual_page))
        self.manual_2.clicked.connect(lambda: self.switchToPage(self.manual_page))

        self.develops_1.clicked.connect(lambda: self.switchToPage(self.develops_page))
        self.develops_2.clicked.connect(lambda: self.switchToPage(self.develops_page))

        self.signout_1.clicked.connect(self.logout)
        self.signout_2.clicked.connect(self.logout)

        self.shutdown.clicked.connect(self.exit)

        # สร้างการแจ้งเตือนส่วนหัว
        self.Title_alert = Alert(self.title)

        # สร้างการแจ้งเตือนแสกน rfid
        self.RFID_alert = Alert(self.rfid_alert)

        # สร้างการแจ้งเตือนอัพเดทข้อมูลการตั้งค่า
        self.updateSettingsData_alert = Alert(self.update_settings)
        self.show_sidebar.setHidden(True)

        self.update_settings.clicked.connect(self.updateSettingsData)
        self.clear_settings.clicked.connect(self.clearSettingsData)
        self.reset_weighing.clicked.connect(self.resetWeighing)

        # เก็บค่า label เริ่มต้นทั้งหมด
        self.initialLabel = {}
        # ค้นหา label ทั้งหมด
        self.findLabels(self)

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
        self.button_exit.clicked.connect(self.run)

        # ไฟล์ข้อมูลการชั่งน้ำหนัก
        self.settingsFile = File(self.settings)

        # ไฟล์ข้อมูลการชั่งน้ำหนัก
        self.OfflineDataFile = File(OfflineDataFile)

        # ไฟล์ข้อมูลการชั่งน้ำหนัก
        self.PackingDataFile = File(PackingDataFile)

        # ไฟล์ข้อมูลรายชื่อ
        self.UserDataFile = File(UserDataFile)

        # ไฟล์ข้อมูลการตั้งค่าการชั่งน้ำหนัก
        self.SettingDataFile = File(SettingDataFile)

        # แสกน rfid
        self.RFID = Rfid()

        # ชั่งน้ำหนัก
        self.Weighing = Weighing(
            widget={
                "weight1": self.weight_1,
                "weight2": self.weight_2,
                "average": self.average,
            }
        )

        # ความหนาของเม็ดยา
        self.GetThickness = Thickness(self)

        self.thickness_val = {}
        movie = QMovie(GifFile)
        self.process_img.setMovie(movie)
        movie.start()

    def findLabels(self, widget, mode: str = "get"):
        """
        ค้นหา QLabel ทั้งหมดที่อยู่ใน widget และดำเนินการตามโหมดที่ระบุ

        Parameters:
            widget (WidgetType): วิดเจ็ตที่ต้องการค้นหา QLabel ในนั้น
            mode (str, optional): โหมดการดำเนินการ ค่าเริ่มต้นคือ "get".
                โหมดที่เป็นไปได้:
                    - "get": ดึง QLabel ที่เกี่ยวข้องกับวิดเจ็ต
                    - "reset": รีเซ็ต QLabel สำหรับวิดเจ็ต
        """
        for child in widget.children():
            if isinstance(child, QLabel):
                if mode == "get":
                    self.initialLabel[child.objectName()] = child.text()
                elif mode == "reset":
                    child.setText(self.initialLabel[child.objectName()])
            else:
                self.findLabels(child, mode)

    def clearSettingsData(self):
        self.SettingDataFile.delete()
        for label_name, label_text in self.initialLabel.items():
            # ค้นหา QLabel ที่มี objectName ตรงกับ label_name
            label = self.frame_10.findChild(QLabel, label_name)
            if label and label.objectName() != "Operator":
                label.setText(label_text)

    # เปลี่ยนหน้าต่างแสดงผล
    def switchToPage(self, page):
        self.stackedWidget.setCurrentWidget(page)

    # เชื่อมต่อฐานข้อมูล
    def dbconnect(self, token, credentials):
        # สร้างอินสแตนซ์ของคลาส Server
        self.server = Server(token, credentials)

        # เรียกใช้เมธอด connect() เพื่อเชื่อมต่อ
        self.service = self.server.connect()

    # อัพเดทฐานข้อมูล
    def updateTabletList(self):
        def format_data(data):
            tabletID = data[0]
            spreadsheetUrl = data[3]
            spreadsheetID = spreadsheetUrl.split('/')[5]
            return {
                "tabletID": tabletID,
                "spreadsheetID": spreadsheetID
            }

        settings = self.settingsFile.read()
        if settings:
            self.mainSpreadsheetId = settings["Main"]["spreadsheetID"]
            self.userDataRange = settings["Main"]["userDataRange"]
            self.TabletListRange = settings["Main"]["TabletListRange"]
            self.settingDataRange = settings["Main"]["settingDataRange"]
            self.tabletID = settings["TabletID"]
            self.current_tabletID_1.setText(f"({self.tabletID})")
            self.current_tabletID_2.setText(self.tabletID)
            
            tabletList = self.server.getData(self.mainSpreadsheetId, self.TabletListRange)
            if tabletList:
                settings["TabletList"] = list(map(format_data, tabletList))
                self.settingsFile.write(settings)
                
                for tabletID in sorted([tablet["tabletID"] for tablet in settings["TabletList"]]):
                    TabletList(self, self.settingsFile, tabletID)


    # อัพเดทข้อมูลรายชื่อ
    def updateUsersData(self):
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

        dataUsers = self.server.getData(self.mainSpreadsheetId, self.userDataRange)
        if dataUsers:
            Lists = list(map(format_data, dataUsers))
            self.UserDataFile.write(Lists)

    # ค้นหา SpreadsheetID จาก tabletID
    def findSpreadsheetID(self, tabletID):
        settings = self.settingsFile.read()
        if settings:
            self.TabletList = settings["TabletList"]
            self.tabletID = settings["TabletID"]

            for tablet in self.TabletList:
                if tablet["tabletID"] == tabletID:
                    return tablet["spreadsheetID"]
            return None
        else:
            return None
     
    # อัพเดทข้อมูลการตั้งค่า
    def updateSettingsData(self):
        settings = self.settingsFile.read()
        if settings:
            self.tabletID = settings["TabletID"]
            sheetDataId = self.findSpreadsheetID(self.tabletID)
            getDataSettings = self.server.getData(sheetDataId, self.settingDataRange)
            if getDataSettings:
                settings = {
                    "productName": getDataSettings[0][0],  # ชื่อยา
                    "lot": getDataSettings[1][0],  # เลขที่ผลิต
                    "balanceID": getDataSettings[2][0],  # เครื่องชั่ง
                    "tabletID": getDataSettings[3][0],  # เครื่องตอก
                    "meanWeight": getDataSettings[4][0],  # น้ำหนักตามทฤษฎี
                    "percentWeightVariation": getDataSettings[5][0],  # เปอร์เซ็นเบี่ยงเบน
                    "meanWeightMin": getDataSettings[6][0],  # ช่วงน้ำหนัก 10 เม็ด(Min.)
                    "meanWeightMax": getDataSettings[7][0],  # ช่วงน้ำหนัก 10 เม็ด(Max.)
                    # ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ (Min.)
                    "meanWeightRegMin": getDataSettings[8][0],
                    # ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ (Max.)
                    "meanWeightRegMax": getDataSettings[9][0],
                    "thicknessMin": getDataSettings[10][0],  # ค่าความหนา(Min.)
                    "thicknessMax": getDataSettings[11][0],  # ค่าความหนา(Max.)
                    "prepared": getDataSettings[12][0],  # ตั้งค่าน้ำหนักโดย
                    "approved": getDataSettings[13][0],  # ตรวจสอบการตั้งค่าโดย
                }

                self.SettingDataFile.write(settings)

            else:
                self.updateSettingsData_alert.alert("เกิดข้อผิดพลาดในการอัพเดท!")

            dataSettings = self.SettingDataFile.read()
            if dataSettings:
                productName = dataSettings["productName"]  # ชื่อยา
                lot = dataSettings["lot"]  # เลขที่ผลิต
                balanceID = dataSettings["balanceID"]  # เครื่องชั่ง
                tabletID = dataSettings["tabletID"]  # เครื่องตอก
                meanWeight = dataSettings["meanWeight"]  # น้ำหนักตามทฤษฎี
                # เปอร์เซ็นเบี่ยงเบน
                percentWeightVariation = dataSettings["percentWeightVariation"]
                meanWeightMin = dataSettings["meanWeightMin"]  # ช่วงน้ำหนัก 10 เม็ด(Min.)
                meanWeightMax = dataSettings["meanWeightMax"]  # ช่วงน้ำหนัก 10 เม็ด(Max.)
                # ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ (Min.)
                meanWeightRegMin = dataSettings["meanWeightRegMin"]
                # ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ (Max.)
                meanWeightRegMax = dataSettings["meanWeightRegMax"]
                thicknessMin = dataSettings["thicknessMin"]  # ค่าความหนา(Min.)
                thicknessMax = dataSettings["thicknessMax"]  # ค่าความหนา(Max.)
                prepared = dataSettings["prepared"]  # ตั้งค่าน้ำหนักโดย
                approved = dataSettings["approved"]  # ตรวจสอบการตั้งค่าโดย

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

    ##########################  screen saver page   ##########################
    screenSaverResult = Signal(int)

    @Slot(int)
    def screenSaver(self):
        """ พักหน้าจอ """
        if self.screenServerTimer > 0:
            self.screenServerTimer -= 1
            self.screenSaverResult.emit(self.screenServerTimer)
        else:
            self.current_page = self.process_page
            self.process_label_line_4.setText("แสกนบัตรพนักงาน...")
            self.switchToPage(self.current_page)
            self.screenServercountdown_timer.stop()  # หยุดนับถอยหลังเมื่อ timeout ถึง 0

    ##########################  login page   ##########################
    loginResult = Signal(dict)  # Define a signal that emits user data

    @Slot(str)
    def login(self, rfid_text):
        """ เข้าสู่ระบบ """

        def rfidCheck(rfid):
            """ ตรวจสอบ RFID ว่ามีในระบบหรือไม่ """
            userDataLists = self.UserDataFile.read()
            for data in userDataLists:
                if data["rfid"] == rfid:
                    return {"usernameTH": data["usernameTH"], "role": data["role"]}
            return None

        self.current_page = self.home_page
        self.switchToPage(self.current_page)
        self.screenServerTimer = 10
        self.rfid.setText(rfid_text)
        userData = rfidCheck(rfid_text)
        QTimer.singleShot(1500, lambda: self.rfid.setText("XXXXXXXXXX"))
        if userData:
            self.screenServercountdown_timer.stop()
            self.RFID_alert.success("กำลังโหลดข้อมูล...")
            self.signout_1.setHidden(False)
            self.signout_2.setHidden(False)
            # Emit the signal with userData
            QTimer.singleShot(1000, lambda: self.loginResult.emit(userData))
            self.packingData["Operator"] = userData["usernameTH"]
            self.Operator.setText(f"{userData['usernameTH']} ({userData['role']})")

            if userData['role'] == "Admin":
                self.clear_settings.setHidden(False)
                self.develops_1.setHidden(False)
                self.develops_2.setHidden(False)
                self.shutdown.setHidden(False)
        else:
            self.RFID.start()
            self.screenServercountdown_timer.start(1000)
            self.RFID_alert.alert("ไม่พบ RFID ในระบบ")

    def logout(self):
        """ ออกจากระบบ """
        self.current_page = self.process_page
        self.switchToPage(self.current_page)
        self.run()

    ##########################  weighing page   ##########################
    getWeighingDataResult = Signal(dict)

    @Slot(dict)
    def getWeighingData(self, weighingData):
        """ ดึงข้อมูลการชั่งน้ำหนัก """

        self.reset_weighing.setHidden(True)
        now = datetime.now()  # current date and time
        timestamp = now.strftime("%d/%m/%Y, %H:%M:%S")

        self.packingData["Timestamp"] = timestamp
        self.packingData["Type"] = "ONLINE"
        self.packingData["Weight"] = weighingData
        QTimer.singleShot(1000, lambda: self.getWeighingDataResult.emit(weighingData))

    def weighingStart(self):
        """ เริ่มฟังชั่นดึงข้อมูลการชั่งน้ำหนัก """
        
        self.updateSettingsData()
        self.current_page = self.weighing_page
        self.switchToPage(self.current_page)
        self.Weighing.get.connect(self.getWeighingData)
        self.Weighing.start()

    def resetWeighing(self):
        self.findLabels(self.weight_group, mode="reset")
        
    ##########################  thickness page   ##########################
    getThicknessDataResult = Signal(dict)

    @Slot(dict)
    def getThicknessData(self, thicknessData):
        self.packingData["Thickness"] = thicknessData
        QTimer.singleShot(1000, lambda: self.getThicknessDataResult.emit(thicknessData))

    def thicknessStart(self):
        self.current_page = self.thickness_page
        self.switchToPage(self.current_page)
        self.GetThickness.get.connect(self.getThicknessData)
        self.GetThickness.start()

    ##########################  characteristics page   ##########################
    characteristicsResult = Signal()

    # เลือกลักษณะเม็ดยา
    def characteristics(self, selected):
        self.packingData["Characteristics"] = selected
        QTimer.singleShot(1000, lambda: self.characteristicsResult.emit())
        QTimer.singleShot(1000, lambda: self.Title_alert.loading("กำลังส่งข้อมูล..."))
        QTimer.singleShot(
            4500, lambda: self.Title_alert.success("ดำเนินการเรียบร้อยแล้ว", style=False)
        )

    def characteristicsStart(self):
        self.current_page = self.characteristics_page
        self.switchToPage(self.current_page)

    ##########################  summary page   ##########################
    countdownResult = Signal(int)

    @Slot(int)
    def updateCountdown(self):
        if self.timer > 0:
            self.timeout.setText(f"{self.timer} s.")
            self.countdownResult.emit(self.timer)
            self.timer -= 1
        else:
            self.countdown_timer.stop()  # หยุดนับถอยหลังเมื่อ timeout ถึง 0
            self.run()

    def SummaryStart(self):
        self.signout_1.setHidden(True)
        self.signout_2.setHidden(True)
        self.PackingDataFile.write(self.packingData)
        self.current_page = self.summary_page
        self.switchToPage(self.current_page)
        self.timer = 180
        self.countdown_timer = QTimer(self)
        self.countdown_timer.timeout.connect(self.updateCountdown)
        self.countdown_timer.start(1000)

    def reset(self):
        self.findLabels(self, mode="reset")

    def exit(self):
        """ ปิดโปรแกรม """
        QApplication.quit()

    def offlineDataCheck(self):
        try:
            offlinData = self.OfflineDataFile.read()
            if offlinData:
                self.Title_alert.alert_always(f"มีไฟล์ออฟไลน์อยู่ {len(offlinData)} ไฟล์")
            else:
                self.Title_alert.stop()
        except FileNotFoundError:
            print("File offline data not found!")
            self.Title_alert.stop()
            pass

    def run(self):
        self.screenServerTimer = 30
        self.screenServercountdown_timer = QTimer(self)
        self.screenServercountdown_timer.timeout.connect(self.screenSaver)
        self.screenServercountdown_timer.start(1000)

        self.offlineDataCheck_timer = QTimer(self)
        self.offlineDataCheck_timer.setInterval(1000)
        self.offlineDataCheck_timer.timeout.connect(self.offlineDataCheck)
        self.offlineDataCheck_timer.start()

        self.reset()
        self.process_label_line_4.setText("กำลังโหลด...")
        self.packingData = {}
        self.dbconnect(self.token, self.credentials)
        self.updateTabletList()
        self.current_page = self.process_page
        self.switchToPage(self.current_page)
        self.updateUsersData()
        self.home_1.setChecked(True)
        self.home_2.setChecked(True)
        self.develops_1.setHidden(True)
        self.develops_2.setHidden(True)
        self.signout_1.setHidden(True)
        self.signout_2.setHidden(True)
        self.clear_settings.setHidden(True)
        self.shutdown.setHidden(True)

        self.current_page = self.home_page
        QTimer.singleShot(3500, lambda: self.switchToPage(self.current_page))

        self.RFID.read.connect(self.login)
        self.RFID.start()
        self.loginResult.connect(self.weighingStart)
        self.getWeighingDataResult.connect(self.thicknessStart)
        self.getThicknessDataResult.connect(self.characteristicsStart)
        self.characteristicsResult.connect(self.SummaryStart)
