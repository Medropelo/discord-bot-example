from __future__ import print_function
from google.oauth2 import service_account
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pandas as pd


"""
The initial lines connect the script with google api, u will need to create a token in https://cloud.google.com/
U can also see the api references and examples in https://developers.google.com/sheets/api/quickstart/python
"""
def main(type):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    SERVICE_ACCOUNT_FILE = """ïnsert google api key"""
    creds = None
    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    #Spreedsheets ID
    SAMPLE_SPREADSHEET_ID = """insert spreadsheet id"""
    SHEETS_RANGE = """insert sheet range (like: sheet!A1:B2)"""
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()


   """
   Recieve data from gsheets to manipulate with pandas. All follow functions does the same thing, but pick up differents values from gsheets,
   this is just an example from what i've use. You will need change values to your own columns names
   """
    if type == 'data':
        SHEETS_RANGE = """insert sheet range (like: sheet!A1:B2)"""
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SHEETS_RANGE).execute()
        values = result.get('values', [])
        for data in values:
            for i in data:
                return i

    if type == 'days':
        SHEETS_RANGE = """insert sheet range (like: sheet!A1:B2)"""
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SHEETS_RANGE).execute()
        values = result.get('values', [])
        for data in values:
            for i in data:
                return i
def dataframe(type, name):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    SERVICE_ACCOUNT_FILE = """ïnsert google api key"""
    creds = None
    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    #Spreedsheets ID
    SAMPLE_SPREADSHEET_ID = """insert spreadsheet id"""
    SHEETS_RANGE = """insert sheet range (like: sheet!A1:B2)"""
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()

    if type == '2dose':
        SHEETS_RANGE = """insert sheet range (like: sheet!A1:B2)"""
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SHEETS_RANGE).execute()
        values = result.get('values', [])
        df = pd.DataFrame(values, columns=['nome', '1dose', '2dose', 'status', 'dias_imunizacao', 'vacina'])
        df = df.loc[((df['nome']).str.upper() == (name).upper()), ['2dose']].values.item()
        return df

    if type == 'days_to':
        SHEETS_RANGE ="""insert sheet range (like: sheet!A1:B2)"""
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SHEETS_RANGE).execute()
        values = result.get('values', [])
        df = pd.DataFrame(values, columns=['nome', '1dose', '2dose', 'status', 'dias_imunizacao', 'vacina'])
        df = df.loc[((df['nome']).str.upper() == (name).upper()), ['dias_imunizacao']].values.item()
        return df
