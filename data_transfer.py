from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class DataTransfer:
    def __init__(self,product_values):
        self.product_values = product_values

    def write_google_datasheet(self):

        SCOPES = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/cloud-platform',
        'https://www.googleapis.com/auth/drive']

        SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
        SAMPLE_RANGE_NAME = 'Class Data!A2:E'

        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'client_secret.json', SCOPES)
                creds = flow.run_local_server(port=8000)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        try:
            service = build('sheets', 'v4', credentials=creds)
            sheet = service.spreadsheets()
            
            body = {
                
                'values': self.product_values
            }
            result = service.spreadsheets().values().append(
                spreadsheetId="1jJT7Y1riKsSOvUidsLyMyuBgl6JZtWSd39lqtF_Q0jU", range="A:G",
                valueInputOption="USER_ENTERED", body=body).execute()
            print('{0} cells updated.'.format(result.get('updatedCells')))
        except HttpError as err:
            print(err)
