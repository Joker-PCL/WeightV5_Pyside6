import json
import pickle
import os.path
import requests
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient import errors


class Server:
    def __init__(self, token=None, credentials=None):
        self.token = token
        self.creds = None
        self.service = None
        self.credentials = credentials
        self.scopes = ["https://www.googleapis.com/auth/spreadsheets"]

    def connect(self):
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

    def getData(self, spreadsheetId: str = None, range: str = None):
        """
        อ่านข้อมูลจาก server \n
        รับค่า spreadsheetId และ range มาเป็น string เพื่อใช้ในการอ่านข้อมูลจาก server

        """
        self.spreadsheetId = spreadsheetId
        self.range = range
        try:
            service = self.connect()
            result = (
                service.spreadsheets()
                .values()
                .get(spreadsheetId=self.spreadsheetId, range=self.range)
                .execute()
            )
            values = result.get("values", [])
            return values
        except Exception as error:
            print(error)
            return None
