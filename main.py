import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(os.environ("GOOGLE_APPLICATION_CREDENTIALS"), scope)
client = gspread.authorize(creds)

sheet = client.open("GAPO").sheet1

sheet.update_cell(1, 1, "I just wrote to a spreadsheet using Python!")