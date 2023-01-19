from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID of a spreadsheet.
SAMPLE_SPREADSHEET_ID = '1o8OyfZbM1hLk01hRgANO1dghs326qD_oEqbYpF4J8tU'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sales!A1:G4").execute()
values = result.get('values', [])

stock_input = input("Add stock for Toyota, Nissan, Porsche, Ford, Mitsubishi and Honda in the format 1,2,3,4,5,6 : ")
aoa = [[stock_input]]

print(aoa)

request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sales!B2:G2", valueInputOption="USER_ENTERED", body={"values":aoa}).execute()
response = request

print(response)