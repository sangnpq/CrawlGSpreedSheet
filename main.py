import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
import requests
import json
from user import User


def download_site(url):
    with requests.get(url) as response:
        if response and response.text and response.text != '':
            item = json.loads(response.text)[0]
            user = User(**item)
            writeSpreedSheet(user, user.data['id'])

def writeSpreedSheet(user, index):
    '''
        Use creds to create a client to interact with the Google Drive API
    '''

    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(os.environ['GOOGLE_APPLICATION_CREDENTIALS'], scope)
    client = gspread.authorize(creds)
    sheet = client.open("GAPO").sheet1

    sheet.insert_row(user.get_value(), index + 1)

if __name__ == "__main__":
    url = "https://api.gapo.vn/main/v1.0/user?id=%d"
    limit = 200000
    sites = [ url %(i + 1) for i in range(0, limit) ]
    for site in sites:
        download_site(site)
