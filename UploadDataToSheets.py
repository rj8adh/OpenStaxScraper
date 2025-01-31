import json
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import time

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
pastQuestionUnit = 1

with open("questionsAndAnswers.json") as f:
    QAdata = json.load(f)

i = 0

while i < len(QAdata):
    if QAdata[i][0] == pastQuestionUnit:
        print(QAdata[i][1])
        for question in QAdata[i][1]:

            if not question:
                i+=1
                break

            answerString = "("
            pageLen = len(QAdata[i][1][question])

            # print(QAdata[i][1])

            for y in range(pageLen - 2):
                answerString += QAdata[i][1][question][y] + "), ("

            answerString += QAdata[i][1][question][pageLen-2] + "), and (" + QAdata[i][1][question][pageLen-1] + ")"
            values.append([question, answerString])
        i+=1

    else:
        body = {'values':values}
        print(f'{values}\n\nUnit{QAdata[i-1][0]}!A1\n')
        pastQuestionUnit = QAdata[i][0]
        # sheet_write = sheet.values().update(spreadsheetId=sheet_id, range=f'Unit{QAdata[i][0]}!A1', valueInputOption='RAW', body=body).execute()
        
        sheet_write = sheet.values().batchUpdate(
        spreadsheetId=sheet_id,
        body={
            "valueInputOption": "RAW",
            "data": [
                {
                    "range": f'Unit{QAdata[i-1][0]}!A1',
                    "values": values  # Replace with your actual data
                }
            ]
        }
).execute()

        # List the mass number and atomic number of carbon-12 and carbon-13, respectively.

f.close()