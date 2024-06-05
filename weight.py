import os
import json
import logging

from ui_weight import Ui_MainWindow
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QGroupBox,
    QVBoxLayout,
)
from PySide6.QtCore import QCoreApplication, QTimer, Signal, Slot, Qt, QSize
from PySide6.QtGui import QMovie, QFont, QCursor, QIcon
from datetime import datetime, timedelta

from src.Alert import Alert
from src.api.File import File
from src.api.Server import Server
from src.api.RFID import Rfid

from src.Weighing import Weighing
from src.Thickness import Thickness
from src.TabletList import TabletList
from src.VideoPlayer import VideoPlayer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GIF_FILE = os.path.join(BASE_DIR, "assets", "gif", "connecting.gif")
MANUAL_VIDEO_FILE = os.path.join(BASE_DIR, "SARAN.mp4")
WEIGHING_DATA_FILE = os.path.join(BASE_DIR, "database", "weighingData.json")
USER_DATA_FILE = os.path.join(BASE_DIR, "database", "usersData.json")
SETTING_DATA_FILE = os.path.join(BASE_DIR, "database", "settings10s.json")
LOGGING_FILE = os.path.join(BASE_DIR, "files", "polipharm.log")
BALANCE_PORT = "COM6"

_LOGGER = logging.getLogger()
_LOGGER.setLevel(logging.DEBUG)
_FILE_HANDLER = logging.FileHandler(LOGGING_FILE, encoding="utf-8")
_FILE_HANDLER.setLevel(logging.DEBUG)
_FORMATTER = logging.Formatter(
    "%(asctime)s %(levelname)s: %(message)s", datefmt="%d-%m-%Y %H:%M:%S"
)
_FILE_HANDLER.setFormatter(_FORMATTER)
_LOGGER.addHandler(_FILE_HANDLER)

_SCREEN_SERVER_TIMEOUT1 = 30  # พักหน้าจอ
_SCREEN_SERVER_TIMEOUT2 = 10  # พักหน้าจอ
_SAMMARY_TIMEOUT = 180  # กำหนดเวลาแสดงหน้า summary


class Weight10s(QMainWindow, Ui_MainWindow):
    def __init__(self, token, credentials, settings):
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

        self.restart_program_1.clicked.connect(self.restart)
        self.restart_program_2.clicked.connect(self.restart)

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
        self.initialStyle = {}
        # ค้นหา label ทั้งหมด
        self.findLabels(self)

        self.button_video_play.clicked.connect(self.manual_video_player)

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
        self.button_exit.clicked.connect(self.reset)

        # ไฟล์ข้อมูลการตั้งค่า
        self.settingsFile = File(self.settings)

        # ไฟล์ข้อมูลการชั่งน้ำหนัก(ออฟไลน์)
        self.WEIGHING_DATA_FILE = File(WEIGHING_DATA_FILE)

        # ไฟล์ข้อมูลรายชื่อ
        self.USER_DATA_FILE = File(USER_DATA_FILE)

        # ไฟล์ข้อมูลการตั้งค่าการชั่งน้ำหนัก
        self.SETTING_DATA_FILE = File(SETTING_DATA_FILE)

        # แสกน rfid
        self.RFID = Rfid()

        # ชั่งน้ำหนัก
        self.Weighing = Weighing(
            port=BALANCE_PORT,
            settingsFile=self.SETTING_DATA_FILE,
            widget={
                "weight1": self.weight_1,
                "weight2": self.weight_2,
                "average": self.average,
            },
        )

        # ความหนาของเม็ดยา
        self.GetThickness = Thickness(self)

        self.thickness_val = {}
        movie = QMovie(GIF_FILE)
        self.process_img.setMovie(movie)
        movie.start()

    def manual_video_player(self):
        if not hasattr(self, "videoPlayer"):
            self.button_video_play.clicked.disconnect(self.manual_video_player)
            self.videoPlayer = VideoPlayer(self.manual_video, "SARAN.mp4")
            self.button_video_play.clicked.connect(self.videoPlayer.media.play)
            self.button_video_pause.clicked.connect(self.videoPlayer.media.pause)
            self.button_video_stop.clicked.connect(self.videoPlayer.media.stop)

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
                    self.initialStyle[child.objectName()] = child.styleSheet()
                elif mode == "reset":
                    child.setText(self.initialLabel[child.objectName()])
                    child.setStyleSheet(self.initialStyle[child.objectName()])
            else:
                self.findLabels(child, mode)

    def clearSettingsData(self):
        print("Clear settings data!")
        _LOGGER.warning(f"Clear settings data by {self.PACKING_DATA['Operator']}")
        self.SETTING_DATA_FILE.delete()
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
        print("Connecting to server")
        # สร้างอินสแตนซ์ของคลาส Server
        self.server = Server(token, credentials)

        # เรียกใช้เมธอด connect() เพื่อเชื่อมต่อ
        self.service = self.server.connect()

    # อัพเดทข้อมูลรายชื่อเครื่องตอก
    def updateTabletList(self):
        print("Update Tablet List")

        def format_data(data):
            tabletID = data[0]
            spreadsheetUrl = data[3]
            spreadsheetID = spreadsheetUrl.split("/")[5]
            return {"tabletID": tabletID, "spreadsheetID": spreadsheetID}

        settings = self.settingsFile.read()
        if settings:
            self.mainSpreadsheetId = settings["Main"]["spreadsheetID"]
            self.userDataRange = settings["Main"]["userDataRange"]
            self.TabletListRange = settings["Main"]["TabletListRange"]
            self.settingDataRange = settings["Main"]["settingDataRange"]
            self.tabletID = settings["TabletID"]
            self.current_tabletID_1.setText(f"({self.tabletID})")
            self.current_tabletID_2.setText(self.tabletID)

            tabletList = self.server.getData(
                self.mainSpreadsheetId, self.TabletListRange
            )
            if tabletList:
                settings["TabletList"] = list(map(format_data, tabletList))
                self.settingsFile.write(settings)

            currunt_tabletList = []
            for child in self.tabletListContents.children():
                if isinstance(child, QGroupBox):
                    currunt_tabletList.append(child.title().replace("เครื่องตอก ", ""))

            settings = self.settingsFile.read()
            for tabletID in sorted(
                [tablet["tabletID"] for tablet in settings["TabletList"]]
            ):
                if not tabletID in currunt_tabletList:
                    TabletList(self, self.settingsFile, tabletID)

    # อัพเดทข้อมูลรายชื่อ
    def updateUsersData(self):
        print("Update users data...")

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
            self.USER_DATA_FILE.write(Lists)
            print("Updated user data file complete")
        else:
            print("Updated user data file not complete")

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
        print("Update settings data...")
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

                self.SETTING_DATA_FILE.write(settings)

            else:
                self.updateSettingsData_alert.alert("เกิดข้อผิดพลาดในการอัพเดท!")

            dataSettings = self.SETTING_DATA_FILE.read()
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

        print("Update settings data complete!")

    ##########################  screen saver page   ##########################
    screenSaverResult = Signal(int)

    @Slot(int)
    def screenSaver(self):
        """พักหน้าจอ"""
        if self.screenServerTimer > 0:
            self.screenServerTimer -= 1
            self.screenSaverResult.emit(self.screenServerTimer)
        else:
            self.home_1.setChecked(True)
            self.home_2.setChecked(True)
            self.current_page = self.process_page
            self.process_label_line_4.setText("แสกนบัตรพนักงาน...")
            self.switchToPage(self.current_page)
            self.screenServercountdown_timer.stop()  # หยุดนับถอยหลังเมื่อ timeout ถึง 0

    ##########################  login page   ##########################
    loginResult = Signal(dict)
    rfid_get_key = Signal(str)

    @Slot(str)
    def login(self, rfid_text):
        """เข้าสู่ระบบ"""

        def rfidCheck(rfid):
            """ตรวจสอบ RFID ว่ามีในระบบหรือไม่"""
            userDataLists = self.USER_DATA_FILE.read()
            for data in userDataLists:
                if data["rfid"] == rfid:
                    return {"usernameTH": data["usernameTH"], "role": data["role"]}
            return None

        print(f"RFID: {rfid_text}\n")
        self.current_page = self.home_page
        self.switchToPage(self.current_page)
        self.screenServerTimer = _SCREEN_SERVER_TIMEOUT2
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
            self.PACKING_DATA["Operator"] = userData["usernameTH"]
            self.Operator.setText(f"{userData['usernameTH']} ({userData['role']})")
            self.scan = False

            _LOGGER.info(f"login: RFID {rfid_text} DETAIL {str(userData)}")

            if userData["role"] == "Admin":
                self.develops_1.setHidden(False)
                self.develops_2.setHidden(False)
                self.clear_settings.setHidden(False)
                self.reset_weighing.setHidden(False)
                self.restart_program_1.setHidden(False)
                self.restart_program_2.setHidden(False)
        else:
            self.RFID.start()
            self.screenServercountdown_timer.start(1000)
            self.RFID_alert.alert("ไม่พบ RFID ในระบบ")

    def logout(self):
        """ออกจากระบบ"""
        self.current_page = self.process_page
        self.switchToPage(self.current_page)
        self.run()

    @Slot(str)
    def keyPressEvent(self, event):
        if self.scan:
            key = event.text()
            if key != "\r":
                self.rfid_key += key

            if key == "\r":
                self.rfid_get_key.emit(self.rfid_key)
                self.rfid_key = ""

    ##########################  weighing page   ##########################
    getWeighingDataResult = Signal(dict)
    getHiddenBtnResult = Signal(bool)

    @Slot(dict)
    def getWeighingData(self, weighingData):
        """ดึงข้อมูลการชั่งน้ำหนัก"""

        print(f"WeighingData: {weighingData}\n")
        self.reset_weighing.setHidden(True)
        now = datetime.now()  # current date and time
        timestamp = now.strftime("%d/%m/%Y, %H:%M:%S")

        self.PACKING_DATA["Timestamp"] = timestamp
        self.PACKING_DATA["Weight"] = weighingData
        QTimer.singleShot(3000, lambda: self.getWeighingDataResult.emit(weighingData))

    @Slot(bool)
    def getHiddenBtn(self, hidden):
        widget_list = [                
            self.signout_1,
                self.signout_2,
                self.restart_program_1,
                self.restart_program_2,
            ]
        
        for w in widget_list:
            if hidden:
                w.setHidden(True)
            else:
                w.setHidden(False)

    def weighingStart(self):
        """เริ่มฟังชั่นดึงข้อมูลการชั่งน้ำหนัก"""

        print("Get weighing data...")
        self.updateSettingsData()
        self.current_page = self.weighing_page
        self.switchToPage(self.current_page)
        if not hasattr(self, "Weighing_called"):
            self.Weighing_called = False

        if not self.Weighing_called:
            self.Weighing_called = True
            self.Weighing.get.connect(self.getWeighingData)
            self.Weighing.hidden.connect(self.getHiddenBtn)
        self.Weighing.start()

    def resetWeighing(self):
        self.findLabels(self.weight_group, mode="reset")
        self.getHiddenBtn(False)
        self.Weighing.weighing.clear()

    ##########################  thickness page   ##########################
    getThicknessDataResult = Signal(dict)

    @Slot(dict)
    def getThicknessData(self, thicknessData):
        print(f"ThicknessData: {thicknessData}\n")
        self.PACKING_DATA["Thickness"] = thicknessData
        QTimer.singleShot(1000, lambda: self.getThicknessDataResult.emit(thicknessData))

    def thicknessStart(self):
        print("Get thickness data...")
        self.current_page = self.thickness_page
        self.switchToPage(self.current_page)
        if not hasattr(self, "GetThickness_called"):
            self.GetThickness_called = False

        if not self.GetThickness_called:
            self.GetThickness_called = True
            self.GetThickness.get.connect(self.getThicknessData)

    ##########################  characteristics page   ##########################
    characteristicsResult = Signal()

    # เลือกลักษณะเม็ดยา
    def characteristics(self, selected):
        print(f"Characteristics: {selected}\n")
        self.PACKING_DATA["Characteristics"] = selected
        QTimer.singleShot(1000, lambda: self.characteristicsResult.emit())

    def characteristicsStart(self):
        print("Get characteristics data...")
        self.current_page = self.characteristics_page
        self.switchToPage(self.current_page)

    ##########################  summary page   ##########################
    countdownResult = Signal(int)
    successResult = Signal()

    @Slot(int)
    def updateCountdown(self):
        if self.summary_timeout >= 0:
            self.timeout.setText(f"{self.summary_timeout} s.")
            self.countdownResult.emit(self.summary_timeout)
            self.summary_timeout -= 1
        else:
            self.successResult.emit()
            self.countdown_timer.stop()  # หยุดนับถอยหลังเมื่อ timeout ถึง 0
            self.run()

    def SummaryStart(self):
        self.signout_1.setHidden(True)
        self.signout_2.setHidden(True)

        self.WEIGHING_DATA_FILE.append(self.PACKING_DATA)
        data = self.PACKING_DATA
        timestamp = data["Timestamp"]
        type = "ONLINE"
        weight1 = data["Weight"]["weight1"]
        weight2 = data["Weight"]["weight2"]
        average = (weight1 + weight2) / 2
        thicknessData = data["Thickness"]

        self.summary_weight_1.setText(f"{weight1:.3f} กรัม")
        self.summary_weight_2.setText(f"{weight2:.3f} กรัม")
        self.summary_average.setText(f"{average:.3f} กรัม")

        settings = self.SETTING_DATA_FILE.read()
        if settings:
            meanWeight = settings["meanWeight"]
            if meanWeight != "xxxxx":
                percentage = round((average / float(meanWeight)) * 100, 2)
                self.summary_percent.setText(f"{percentage:.2f}%")

        thickness_data_obj = []
        for i in range(1, 11):
            thickness = thicknessData[f"number_{i}"]
            if thickness != "-":
                thickness_widget = getattr(self, f"thickness_summary_{i}")
                thickness_widget.setText(thickness)
                thickness_data_obj.append(round(float(thickness), 2))

        if thickness_data_obj:
            self.summary_min_thickness.setText(f"{min(thickness_data_obj):.2f} mm.")
            self.summary_max_thickness.setText(f"{max(thickness_data_obj):.2f} mm.")

        self.current_page = self.summary_page
        self.switchToPage(self.current_page)
        self.summary_timeout = _SAMMARY_TIMEOUT
        if not hasattr(self, "countdown_timer"):
            self.countdown_timer = QTimer(self)
            self.countdown_timer.timeout.connect(self.updateCountdown)
        self.countdown_timer.start(1000)

    ##########################  Send data to server   ##########################
    def sendDataToServer(self, data):
        print("Send data to server...")
        self.Title_alert.loading("กำลังส่งข้อมูล...")
        try:
            timestamp = data["Timestamp"]
            type = "ONLINE"
            weight1 = data["Weight"]["weight1"]
            weight2 = data["Weight"]["weight2"]
            average = None
            percentage = None
            characteristics = data["Characteristics"]
            operator = data["Operator"]
            inspactor = None
            thicknessData = data["Thickness"]

            packing_data = [
                timestamp,
                type,
                weight1,
                weight2,
                average,
                percentage,
                characteristics,
                operator,
                inspactor,
            ]

            for i in range(1, 11):
                packing_data.append(thicknessData[f"number_{i}"])

            print(f"PackingData: {packing_data}\n")
            _LOGGER.debug(f"PackingData: {packing_data}")
            settings = self.settingsFile.read()
            if settings:
                self.tabletID = settings["TabletID"]
                sheetDataId = self.findSpreadsheetID(self.tabletID)
                rangeData = settings["Main"]["weighingDataRange"]
                result = self.server.sendData(sheetDataId, rangeData, packing_data)
                if result:
                    self.Title_alert.success("ดำเนินการเรียบร้อยแล้ว", 3000, style=False)
                else:
                    self.Title_alert.success(
                        "เกิดข้อผิดพลาดในการส่งข้อมูล", 3000, style=False
                    )

        except Exception as e:
            print("Error sending data to server: ", e)
            return False
    
    ##########################  weight10s' ##########################
    def reset(self):
        if hasattr(self, "countdown_timer"):
            self.countdown_timer.stop()
        self.findLabels(self, mode="reset")
        self.run()

    def restart(self):
        """รีสตาร์ทโปรแกรม"""
        QApplication.quit()

    def exit(self):
        """ปิดโปรแกรม"""
        QApplication.quit()

    sendDataToServerStatus = Signal()
    def offlineDataCheck(self):
        try:
            offline_count = 0
            weighing_data = self.WEIGHING_DATA_FILE.read()
            if weighing_data:
                for data in weighing_data:
                    current_time = datetime.now()
                    timestamp_str = data['Timestamp']
                    timestamp = datetime.strptime(timestamp_str, '%d/%m/%Y, %H:%M:%S')
                    if current_time - timestamp > timedelta(minutes=15):
                        # self.sendDataToServer(data)
                        offline_count += 1

                print(offline_count)
                self.Title_alert.alert_always(f"มีไฟล์ออฟไลน์อยู่ {offline_count} ไฟล์")
                self.offlineDataCheck_timer.stop()
            else:
                self.offlineDataCheck_timer.setInterval(3000)
                self.Title_alert.stop()
        except FileNotFoundError:
            print("File offline data not found!")
            self.Title_alert.stop()
            pass
    
    def run(self):
        print("Weight10s' is running...")
        # Valiable parameters
        self.PACKING_DATA = {}
        self.SEND_DATA_TO_SERVER_STATUS = True

        self.screenServerTimer = _SCREEN_SERVER_TIMEOUT1
        if not hasattr(self, "screenServercountdown_timer"):
            self.screenServercountdown_timer = QTimer(self)
            self.screenServercountdown_timer.timeout.connect(self.screenSaver)
        self.screenServercountdown_timer.start(1000)

        if not hasattr(self, "offlineDataCheck_timer"):
            self.offlineDataCheck_timer = QTimer(self)
            self.offlineDataCheck_timer.timeout.connect(self.offlineDataCheck)
        self.offlineDataCheck_timer.start()

        self.process_label_line_4.setText("กำลังโหลด...")
        self.PACKING_DATA = {}
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
        self.reset_weighing.setHidden(True)
        self.reset_weighing.setHidden(True)
        self.restart_program_1.setHidden(False)
        self.restart_program_2.setHidden(False)

        self.current_page = self.home_page
        QTimer.singleShot(3500, lambda: self.switchToPage(self.current_page))

        self.scan = True
        self.rfid_key = ""

        if not hasattr(self, "FirstConnect"):
            self.FirstConnect = True

        if self.FirstConnect:
            self.FirstConnect = False
            self.rfid_get_key.connect(self.login)
            self.loginResult.connect(self.weighingStart)
            self.getWeighingDataResult.connect(self.thicknessStart)
            self.getThicknessDataResult.connect(self.characteristicsStart)
            self.characteristicsResult.connect(self.SummaryStart)
            self.successResult.connect(self.reset)
