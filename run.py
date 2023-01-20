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
st_mitsu = input("Add stock for Mitsubishi: ")
st_honda = input("Add stock for Honda: ")
st_update = [[st_toyota, st_nissan, st_porsche, st_ford, st_mitsu, st_honda]]

print(st_update)
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sales!B2:G2", valueInputOption="USER_ENTERED", body={"values":st_update}).execute()

sale_toyota = input("Add sales data for Toyota: ")
sale_nissan = input("Add sales data for Nissan: ")
sale_porsche = input("Add sales data for Porsche: ")
sale_ford = input("Add sales data for Ford: ")
sale_mitsu = input("Add sales data for Mitsubishi: ")
sale_honda = input("Add sales data for Honda: ")
sale_update = [[sale_toyota, sale_nissan, sale_porsche, sale_ford, sale_mitsu, sale_honda]]

print(sale_update)
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sales!B3:G3", valueInputOption="USER_ENTERED", body={"values":sale_update}).execute()

eom_stock = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sales!A4:G4").execute()

eom_values = eom_stock.get('values', [])
print(eom_values)

eom_toyota = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sales!B4").execute()
eom_toyota_values = eom_toyota.get('values')
toyota_lists = eom_toyota_values
toyota_string_version = ''.join([''.join(map(str, sublist)) for sublist in toyota_lists])
toyota_int_version = int(toyota_string_version)

eom_nissan = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sales!C4").execute()
eom_nissan_values = eom_nissan.get('values')
nissan_lists = eom_nissan_values
nissan_string_version = ''.join([''.join(map(str, sublist)) for sublist in nissan_lists])
nissan_int_version = int(nissan_string_version)

eom_porsche = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sales!D4").execute()
eom_porsche_values = eom_porsche.get('values')
porsche_lists = eom_porsche_values
porsche_string_version = ''.join([''.join(map(str, sublist)) for sublist in porsche_lists])
porsche_int_version = int(porsche_string_version)

eom_ford = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sales!E4").execute()
eom_ford_values = eom_ford.get('values')
ford_lists = eom_ford_values
ford_string_version = ''.join([''.join(map(str, sublist)) for sublist in ford_lists])
ford_int_version = int(ford_string_version)

eom_mitsu = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sales!F4").execute()
eom_mitsu_values = eom_mitsu.get('values')
mitsu_lists = eom_mitsu_values
mitsu_string_version = ''.join([''.join(map(str, sublist)) for sublist in mitsu_lists])
mitsu_int_version = int(mitsu_string_version)

eom_honda = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sales!G4").execute()
eom_honda_values = eom_honda.get('values')
honda_lists = eom_honda_values
honda_string_version = ''.join([''.join(map(str, sublist)) for sublist in honda_lists])
honda_int_version = int(honda_string_version)

print(toyota_int_version, nissan_int_version, porsche_int_version, ford_int_version, mitsu_int_version, honda_int_version)

request_toyota = [[int(sale_toyota) - toyota_int_version]]
order_toyota = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="orders!B2", valueInputOption="USER_ENTERED", body={"values":request_toyota}).execute()
print(request_toyota)