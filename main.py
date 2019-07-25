import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
import requests
import json
from user import User


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(os.environ['GOOGLE_APPLICATION_CREDENTIALS'], scope)
client = gspread.authorize(creds)
sheet = client.open("GAPO")

def download_site(url, data):
    with requests.get(url) as response:
        if response and response.text and response.text != '':
            item = json.loads(response.text)
            if len(item) > 0:
                user = User(**item[0])
                data.append(user.get_value())

def writeSpreedSheet(data, index):
    '''
        Use creds to create a client to interact with the Google Drive API
    '''
    sheet.values_update('1!A%d'  % index, params={'valueInputOption': 'RAW'}, body={ 'values': data })


if __name__ == "__main__":
    url = "https://api.gapo.vn/main/v1.0/user?id=%d"
    limit = 200000
    data = []
    curr_row = 2
    sites = [ url %(i + 1) for i in range(0, limit) ]
    for i in range(1, limit):
        if i%1000 == 0:
            print "---%d---" % curr_row
            writeSpreedSheet(data, curr_row)
            curr_row += len(data)
            data = []
        download_site(url % i, data)
