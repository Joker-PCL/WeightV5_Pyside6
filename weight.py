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

_LOGGER = logging.getLogger()
_LOGGER.setLevel(logging.DEBUG)
_FILE_HANDLER = logging.FileHandler(LOGGING_FILE, encoding="utf-8")
_FILE_HANDLER.setLevel(logging.DEBUG)
_FORMATTER = logging.Formatter(
    "%(asctime)s %(levelname)s: %(message)s", datefmt="%d-%m-%Y %H:%M:%S"
)
_FILE_HANDLER.setFormatter(_FORMATTER)
_LOGGER.addHandler(_FILE_HANDLER)

_OFFLINE_CHECK_TIME = 15 # min ตั้งค่าเวลากำหนดให้เป็นข้อมูล Offline
_WEIGHING_DATA_FILE_CHECK_TIME = 5000 # millisec ระยะเวลาตรวจสอบไฟล์ข้อมูลการชั่ง
_SCREEN_SERVER_TIMEOUT1 = 30  # sec พักหน้าจอ
_SCREEN_SERVER_TIMEOUT2 = 10  # sec พักหน้าจอ
_SAMMARY_TIMEOUT = 180  # sec กำหนดเวลาแสดงหน้า summary


class Weight10s(QMainWindow, Ui_MainWindow):
    def __init__(self, token, credentials, settings, balancePort):
        """
        token = google.auth.token
        credentials = google.oauth2.credentials.Credentials
        settings = ไฟล์ตั้งค่าโปรแกรม **/files/settings.json
        balancePort = พอร์ต RS232 ** Windows("COM6"), Linux("/dev/ttyUSB0")
        """
        super().__init__()

        self.token = token
        self.credentials = credentials
        self.settings = settings
        self.balancePort = balancePort

        self.setupUi(self)
        self.current_page = self.home_page
        self.home_1.clicked.connect(lambda: self.switchToPage(self.current_page))
        self.home_2.clicked.connect(lambda: self.switchToPage(self.current_page))

        self.manual_1.clicked.connect(lambda: self.switchToPage(self.manual_page))
        self.manual_2.clicked.connect(lambda: self.switchToPage(self.manual_page))

        self.develops_1.clicked.connect(lambda: self.switchToPage(self.develops_page))
        self.develops_2.clicked.connect(lambda: self.switchToPage(self.develops_page))

        self.signout_1.clicked.connect(self.reset)
        self.signout_2.clicked.connect(self.reset)

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
            port=self.balancePort,
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

    ##########################  อัพเดทข้อมูลรายชื่อเครื่องตอก   ##########################
    updateTabletListResult = Signal()
    def updateTabletList(self):
        print("*** Update tablet list...")
        settings = self.settingsFile.read()
        if settings:
            self.mainSpreadsheetId = settings["Main"]["spreadsheetID"]
            self.userDataRange = settings["Main"]["userDataRange"]
            self.TabletListRange = settings["Main"]["TabletListRange"]
            self.settingDataRange = settings["Main"]["settingDataRange"]
            self.tabletID = settings["TabletID"]
            self.current_tabletID_1.setText(f"({self.tabletID})")
            self.current_tabletID_2.setText(self.tabletID)

        if not hasattr(self, "getTabletList"):
            self.getTabletList = Server(self.token, self.credentials)
            self.getTabletList.get.connect(self._updateTabletList)

        self.getTabletList.getData(self.mainSpreadsheetId, self.TabletListRange)

    @Slot(object)
    def _updateTabletList(self, tabletList):
        self.updateTabletListResult.emit()
        print("*** Update tablet list complete")

        def format_data(data):
            tabletID = data[0]
            spreadsheetUrl = data[3]
            spreadsheetID = spreadsheetUrl.split("/")[5]
            return {"tabletID": tabletID, "spreadsheetID": spreadsheetID}

        settings = self.settingsFile.read()
        if settings:
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

    ##########################  อัพเดทข้อมูลรายชื่อ   ##########################
    updateUsersDataResult = Signal()
    def updateUsersData(self):
        print("*** Update settings data...")
        if not hasattr(self, "getUserData"):
            self.getUserData = Server(self.token, self.credentials)
            self.getUserData.get.connect(self._updateUsersData)

        self.getUserData.getData(self.mainSpreadsheetId, self.userDataRange)

    @Slot(object)
    def _updateUsersData(self, dataUsers):
        self.updateUsersDataResult.emit()

        print("*** Update users data complete")

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

    ##########################   อัพเดทข้อมูลการตั้งค่า   ##########################
    updateSettingsDataResult = Signal()
    def updateSettingsData(self):
        print("*** Update settings data...")
        settingsFile = self.settingsFile.read()
        if settingsFile:
            self.tabletID = settingsFile["TabletID"]
            sheetDataId = self.findSpreadsheetID(self.tabletID)
            if not hasattr(self, "getSettingsData"):
                self.getSettingsData = Server(self.token, self.credentials)
                self.getSettingsData.get.connect(self._updateSettingsData)

            self.getSettingsData.getData(sheetDataId, self.settingDataRange)

    @Slot(object)
    def _updateSettingsData(self, result):
        self.updateSettingsDataResult.emit()

        if result:
            settings = {
                "productName": result[0][0],  # ชื่อยา
                "lot": result[1][0],  # เลขที่ผลิต
                "balanceID": result[2][0],  # เครื่องชั่ง
                "tabletID": result[3][0],  # เครื่องตอก
                "meanWeight": result[4][0],  # น้ำหนักตามทฤษฎี
                "percentWeightVariation": result[5][0],  # เปอร์เซ็นเบี่ยงเบน
                "meanWeightMin": result[6][0],  # ช่วงน้ำหนัก 10 เม็ด(Min.)
                "meanWeightMax": result[7][0],  # ช่วงน้ำหนัก 10 เม็ด(Max.)
                # ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ (Min.)
                "meanWeightRegMin": result[8][0],
                # ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ (Max.)
                "meanWeightRegMax": result[9][0],
                "thicknessMin": result[10][0],  # ค่าความหนา(Min.)
                "thicknessMax": result[11][0],  # ค่าความหนา(Max.)
                "prepared": result[12][0],  # ตั้งค่าน้ำหนักโดย
                "approved": result[13][0],  # ตรวจสอบการตั้งค่าโดย
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

        print("*** Update settings data complete!")

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
    loginResult = Signal()
    rfidGetKey = Signal(str)

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

        print(f"RFID: {rfid_text}")
        self.current_page = self.home_page
        self.switchToPage(self.current_page)
        self.screenServerTimer = _SCREEN_SERVER_TIMEOUT2
        self.rfid.setText(rfid_text)
        userData = rfidCheck(rfid_text)
        
        if userData:
            self.screenServercountdown_timer.stop()
            self.RFID_alert.loading("กำลังโหลดข้อมูล...")
            self.signout_1.setHidden(False)
            self.signout_2.setHidden(False)
            QTimer.singleShot(1000, lambda: self.loginResult.emit())
            self.PACKING_DATA["Operator"] = userData["usernameTH"]
            self.Operator.setText(f"{userData['usernameTH']} ({userData['role']})")
            self.RFID_SCAN = False

            _LOGGER.info(f"login: RFID {rfid_text} DETAIL {str(userData)}")

            if userData["role"] == "Admin":
                self.develops_1.setHidden(False)
                self.develops_2.setHidden(False)
                self.clear_settings.setHidden(False)
                self.reset_weighing.setHidden(False)
                self.restart_program_1.setHidden(False)
                self.restart_program_2.setHidden(False)
        else:
            self.screenServercountdown_timer.start(1000)
            self.RFID_alert.alert("ไม่พบ RFID ในระบบ")
            QTimer.singleShot(1500, lambda: self.rfid.setText("XXXXXXXXXX"))
            QTimer.singleShot(1500, self.RFID.start)

    def loginStart(self):
        self.RFID_SCAN = True
        self.current_page = self.home_page
        QTimer.singleShot(2000, lambda: self.switchToPage(self.current_page))

    def keyPressEvent(self, event):
        if self.RFID_SCAN:
            key = event.text()
            if key != "\r":
                self.RFID_KEY += key

            if key == "\r":
                self.rfidGetKey.emit(self.RFID_KEY)
                self.RFID_KEY = ""

    ##########################  weighing page   ##########################
    getWeighingDataResult = Signal(dict)
    hiddenBtnResult = Signal(bool)

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
    def hiddenBtn(self, hidden):
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
        self.current_page = self.weighing_page
        self.switchToPage(self.current_page)
        if not hasattr(self, "Weighing_called"):
            self.Weighing_called = False

        if not self.Weighing_called:
            self.Weighing_called = True
            self.Weighing.get.connect(self.getWeighingData)
            self.Weighing.hidden.connect(self.hiddenBtn)
        else:
            self.Weighing.weighing.clear()
            self.Weighing.isRunning()

        self.Weighing.start()

    def resetWeighing(self):
        self.findLabels(self.weight_group, mode="reset")
        self.hiddenBtn(False)
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

    def summaryStart(self):
        self.signout_1.setHidden(True)
        self.signout_2.setHidden(True)

        self.PACKING_DATA["Type"] = "ONLINE"
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
    sendDataToServerResult = Signal(bool)

    def sendDataToServer(self):
        self.Title_alert.loading("กำลังส่งข้อมูล...", False)

        try:
            self.offline_count = 0
            weighing_data = self.WEIGHING_DATA_FILE.read()
            if weighing_data:
                print("*** Send data to server...")
                for data in weighing_data:
                    current_time = datetime.now()
                    timestamp_str = data["Timestamp"]
                    timestamp = datetime.strptime(timestamp_str, "%d/%m/%Y, %H:%M:%S")
                    if current_time - timestamp > timedelta(minutes=_OFFLINE_CHECK_TIME):
                        data["Type"] = "OFFLINE"
                        self.offline_count += 1

                self.WEIGHING_DATA_FILE.write(weighing_data)
                self.Title_alert.alert_always(f"กำลังส่งข้อมูล...", False)
                self.sendDataToServer_timer.stop()

                settings = self.settingsFile.read()
                if settings:
                    self.tabletID = settings["TabletID"]
                    sheetDataId = self.findSpreadsheetID(self.tabletID)
                    rangeData = settings["Main"]["weighingDataRange"]
                    if not hasattr(self, "postDataToServer"):
                        self.postDataToServer = Server(self.token, self.credentials)
                        self.postDataToServer.get.connect(self._sendDataToServer)

                    self.postDataToServer.postData(sheetDataId, rangeData, self.WEIGHING_DATA_FILE.read())
            else:
                self.sendDataToServer_timer.setInterval(_WEIGHING_DATA_FILE_CHECK_TIME)
                self.Title_alert.stop()
        except FileNotFoundError:
            print("File data not found!")
            self.Title_alert.stop()
            pass
    
    @Slot(bool)
    def _sendDataToServer(self, result=False):
        if result:
            self.Title_alert.success("ดำเนินการเรียบร้อยแล้ว", 3000)
            self.WEIGHING_DATA_FILE.delete()
            self.sendDataToServer_timer.start(10000)
        else:
            self.Title_alert.alert("เกิดข้อผิดพลาดในการส่งข้อมูล", 3000)
            if self.offline_count:
                QTimer.singleShot(3000, lambda: self.Title_alert.alert_always(f"มีไฟล์ออฟไลน์อยู่ {self.offline_count} ไฟล์"))
            self.sendDataToServer_timer.start(10000)
    
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

    def run(self):
        print("Weight10s' is running...")
        # Valiable parameters
        self.PACKING_DATA = {}
        self.SEND_DATA_TO_SERVER_STATUS = True
        self.RFID_SCAN = False
        self.RFID_KEY = ""

        # พักหน้าจอ
        self.screenServerTimer = _SCREEN_SERVER_TIMEOUT1
        if not hasattr(self, "screenServercountdown_timer"):
            self.screenServercountdown_timer = QTimer(self)
            self.screenServercountdown_timer.timeout.connect(self.screenSaver)
        self.screenServercountdown_timer.start(1000)

        # ส่งข้อมูลไปบันทึกยัง sever
        if not hasattr(self, "offlineDataCheck_timer"):
            self.sendDataToServer_timer = QTimer(self)
            self.sendDataToServer_timer.timeout.connect(self.sendDataToServer)
        self.sendDataToServer_timer.start()

        # โหลดข้อมูลหน้าแรก
        self.current_page = self.process_page
        self.switchToPage(self.current_page)
        self.process_label_line_4.setText("กำลังโหลด...")
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

        # อัพเดทข้อมูล
        self.updateTabletList()
        if not hasattr(self, "FirstConnect"):
            self.FirstConnect = True

        if self.FirstConnect:
            self.FirstConnect = False
            self.updateTabletListResult.connect(self.updateUsersData)
            self.updateUsersDataResult.connect(self.loginStart)
            self.rfidGetKey.connect(self.login)
            self.loginResult.connect(self.updateSettingsData)
            self.updateSettingsDataResult.connect(self.weighingStart)
            self.getWeighingDataResult.connect(self.thicknessStart)
            self.getThicknessDataResult.connect(self.characteristicsStart)
            self.characteristicsResult.connect(self.summaryStart)
            self.successResult.connect(self.reset)