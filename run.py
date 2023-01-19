from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

credentials = None
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID of a spreadsheet.
SAMPLE_SPREADSHEET_ID = '1o8OyfZbM1hLk01hRgANO1dghs326qD_oEqbYpF4J8tU'
  
  
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])

if not values:
    print('No data found.')
    return

print('Name, Major:')
for row in values:
    # Print columns A and E, which correspond to indices 0 and 4.
    print('%s, %s' % (row[0], row[4]))
except HttpError as err:
print(err)