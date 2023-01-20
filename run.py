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

st_toyota = input("Add stock for Toyota: ")
st_nissan = input("Add stock for Nissan: ")
st_porsche = input("Add stock for Porsche: ")
st_ford = input("Add stock for Ford: ")
st_mitsubishi = input("Add stock for Mitsubishi: ")
st_honda = input("Add stock for Honda: ")
st_update = [[st_toyota,st_nissan,st_porsche,st_ford,st_mitsubishi,st_honda]]

print(st_update)

request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sales!B2:G2", valueInputOption="USER_ENTERED", body={"values":st_update}).execute()
response = request

print(response)