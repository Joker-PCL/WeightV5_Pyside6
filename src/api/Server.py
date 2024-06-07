import logging
import pickle
import os.path
import requests
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient import errors
from PySide6.QtCore import QThread, Signal, Slot

_LOGGER = logging.getLogger(__name__)

########################## คลาสดึงข้อมูล ##########################
class GetData(QThread):
    get = Signal(object)

    def __init__(self, service, spreadsheetId=None, rangeData=None):
        super().__init__()
        self.service = service
        self.spreadsheetId = spreadsheetId
        self.rangeData = rangeData

    def run(self):
        try:
            result = (
                self.service.spreadsheets()
                .values()
                .get(spreadsheetId=self.spreadsheetId, range=self.rangeData)
                .execute()
            )

            values = result.get("values", [])
            self.get.emit(values)
        except Exception as error:
            print(error)
            self.get.emit([])


########################## คลาสส่งข้อมูล ##########################
class PostData(QThread):
    post = Signal(bool)

    def __init__(self, service, spreadsheetId=None, rangeData=None, data=None):
        super().__init__()
        self.service = service
        self.spreadsheetId = spreadsheetId
        self.rangeData = rangeData
        self.data = data

    def run(self):
        try:
            packing_data = []

            for _data in self.data:
                timestamp = _data["Timestamp"]
                type = _data["Type"]
                weight1 = _data["Weight"]["weight1"]
                weight2 = _data["Weight"]["weight2"]
                average = None
                percentage = None
                characteristics = _data["Characteristics"]
                operator = _data["Operator"]
                inspactor = None
                thicknessData = _data["Thickness"]

                packing_cache = [
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
                    packing_cache.append(thicknessData[f"number_{i}"])

                packing_data.append(packing_cache)
            
            try:
                response = (
                    self.service.spreadsheets()
                    .values()
                    .append(
                        spreadsheetId=self.spreadsheetId,
                        range=self.rangeData,
                        body={"majorDimension": "ROWS", "values": packing_data},
                        valueInputOption="USER_ENTERED",
                    )
                    .execute()
                )

            except Exception as e:
                _LOGGER.error(f"Send data to server: {packing_data} \n {e}")
                self.post.emit(False)
                return
            
            _LOGGER.debug(f"Send data to server: {packing_data}")
            self.post.emit(True)

        except Exception as e:
            _LOGGER.error(f"sendData_sheets: {self.data} \n {e}")
            self.post.emit(False)


class Server(QThread):
    print("*** Server is running...")
    get = Signal(object)
    post = Signal(object)

    def __init__(self, token=None, credentials=None):
        super().__init__()
        self.token = token
        self.credentials = credentials
        self.scopes = ["https://www.googleapis.com/auth/spreadsheets"]

    def connection(self):
        try:
            creds = None
            if os.path.exists(self.token):
                with open(self.token, "rb") as token:
                    creds = pickle.load(token)
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        self.credentials, self.scopes
                    )
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open(self.token, "wb") as token:
                    pickle.dump(creds, token)

            service = build("sheets", "v4", credentials=creds)
            return service

        except Exception as error:
            print(error)
            return None

    ##########################  ดึงข้อมูลจาก server  ##########################
    def getData(self, sheetDataId, settingDataRange):
        """
        อ่านข้อมูลจาก server \n
        รับค่า spreadsheetId และ range มาเป็น string เพื่อใช้ในการอ่านข้อมูลจาก server
        """
        try:
            service = self.connection()
            if not hasattr(self, "_getData_"):
                self._getData_ = GetData(service, sheetDataId, settingDataRange)
                self._getData_.get.connect(self._getData)
            self._getData_.start()
        except Exception as error:
            print(error)
            self.get.emit([])

    @Slot(object)
    def _getData(self, result):
        if hasattr(self, "_getData_"):
            del self._getData_

        self.get.emit(result)

    ##########################  ส่งข้อมูลไปยัง server  ##########################
    def postData(self, sheetDataId, settingDataRange, data):
        """
        ส่งข้อมูลไปยัง server \n
        รับค่า spreadsheetId และ range มาเป็น string \n
        และ data มาเป็น object เพื่อใช้ในการส่งข้อมูลไปยัง server
        """

        try:
            service = self.connection()
            if not hasattr(self, "data"):
                self._postData_ = PostData(service, sheetDataId, settingDataRange, data)
                self._postData_.post.connect(self._postData)
            self._postData_.start()
        except Exception as error:
            print(error)
            self.post.emit([])

    @Slot(bool)
    def _postData(self, result):
        if hasattr(self, "_postData_"):
            del self._postData_

        self.get.emit(result)
