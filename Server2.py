import json
import pickle
import os.path
import requests
import logging
from time import sleep

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient import errors

from PySide6.QtCore import QThread, Signal, Slot


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STYLE = os.path.join(BASE_DIR, "style.qss")
ICON = os.path.join(BASE_DIR, "assets", "images", "scale.png")

TOKEN = os.path.join(BASE_DIR, "files", "token.pickle")
CREDENTIALS = os.path.join(BASE_DIR, "files", "credentials.json")
SETTINGS = os.path.join(BASE_DIR, "files", "settings.json")

MAIN_SPREADSHEET_ID = "1CP7r6TBxu_5HTqhE4mJ4-CPn_0XaxhET1pPp0WxTtRY"
USER_DATA_RANGE = "User!A3:F"
SPREADSHEET_ID = "1VecUHiEccSf7Z9TqO-ECSk_q0rDmXC2FT5TjSQL8GcY"
SETTINGS_RANGE = "Setting!B2:B17"

from PySide6.QtCore import QThread, Signal, Slot

class Server(QThread):
    get = Signal(dict)

    def __init__(self, token=None, credentials=None, spreadsheetId=None, rangeData=None):
        super().__init__()
        self.token = token
        self.creds = None
        self.service = None
        self.credentials = credentials
        self.spreadsheetId = spreadsheetId
        self.rangeData = rangeData
        self.scopes = ["https://www.googleapis.com/auth/spreadsheets"]

    def dbconnect(self):
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

    def run(self):
        """
        อ่านข้อมูลจาก server \n
        รับค่า spreadsheetId และ range มาเป็น string เพื่อใช้ในการอ่านข้อมูลจาก server

        """
        print("Server is running..")
        while True:
            try:
                service = self.dbconnect()
                result = (
                    service.spreadsheets()
                    .values()
                    .get(spreadsheetId=self.spreadsheetId, range=self.rangeData)
                    .execute()
                )
                values = result.get("values", [])
                print(values)
                self.get.emit({'values': values})
            except Exception as error:
                print(error)
                self.get.emit({'values': ""})
            
            sleep(3)

class test_data_sheets():
    def __init__(self):
        self.server = Server(TOKEN, CREDENTIALS, MAIN_SPREADSHEET_ID, USER_DATA_RANGE)
        self.server.dbconnect()
        self.server.get.connect(self.test)
        self.server.start()

    @Slot(dict)
    def test(self, data):
        print(data)

def main():
    test = test_data_sheets()

    while True:
        print("Testing")
        sleep(0.5)

if __name__ == "__main__":
    main()