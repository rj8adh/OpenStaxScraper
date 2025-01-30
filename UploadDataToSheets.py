import json
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SERVICE_ACCOUNT_FILE = "cloud_key.json"

credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('sheets', 'v4', credentials=credentials)

sheet = service.spreadsheets()

sheet_id = '16M3Pv_2M1YG90w0b1jojjzSDFiWP4gyqBPUsPJcIAWc'

# range = 'A1:A5'
# sheet_read = sheet.values().get(spreadsheetId=sheet_id, range=range).execute()

# values = sheet_read.get('values', [])
# for row in values:
#     print(row)

values = []

with open("questionsAndAnswers.json") as f:
    QAdata = json.load(f)

for questionPage in QAdata:
    for question in questionPage:
        answerString = "("
        pageLen = len(questionPage[question])
        for i in range(pageLen - 2):
            answerString += questionPage[question][i] + "), ("
        answerString += questionPage[question][pageLen-2] + "), and (" + questionPage[question][pageLen-1] + ")"
        values.append([question, answerString])

body = {'values':values}

sheet_write = sheet.values().update(spreadsheetId=sheet_id, range='A1', valueInputOption='RAW', body=body).execute()
f.close()
