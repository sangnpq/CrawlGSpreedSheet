import gspread
from oauth2client.service_account import ServiceAccountCredentials

my_file_key = '10xyHnFQbrYy7OGNCr0ayP2CVSVevbItykm4lhK18f4k'

# your auth here
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

gc = gspread.authorize(credentials)

spreadsheet = gc.open_by_key(my_file_key) # key to your spreadsheet here
ws = spreadsheet.get_worksheet(0)

# Select a range
cell_list = ws.range('A1:C7')

for cell in cell_list:
    cell.value = 'abcdef'

# Update in batch
ws.update_cells(cell_list)