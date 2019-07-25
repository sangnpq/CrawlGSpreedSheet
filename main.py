import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
import concurrent.futures
import requests
import threading
import time
import json
from user import User

thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        item = json.loads(response.text)[0]
        user = User(**item)
        writeSpreedSheet(user, user.data['id'])


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(download_site, sites)


def writeSpreedSheet(user, index):
    '''
        Use creds to create a client to interact with the Google Drive API
    '''

    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(os.environ['GOOGLE_APPLICATION_CREDENTIALS'], scope)
    client = gspread.authorize(creds)
    sheet = client.open("GAPO").sheet1

    sheet.insert_row(user.get_value, index + 1)

if __name__ == "__main__":
    url = "https://api.gapo.vn/main/v1.0/user?id=%d"
    limit = 200000
    sites = [ url %(i + 1) for i in range(0, limit) ]

    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
