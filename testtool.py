from __future__ import print_function
import pickle
import os.path
import io
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import httplib2
import os
import random
import sys
import time

from apiclient.discovery import build as discovery_build
from apiclient.errors import HttpError
from apiclient.http import MediaFileUpload
from apiclient.http import MediaIoBaseDownload
from json import dumps as json_dumps

from apiclient import errors


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    # Drive v3 API     

    # Create a file (Upload)
    if sys.argv[1]== 'put':
        media_body = MediaFileUpload(sys.argv[3], mimetype='application/octet-stream', chunksize=1024*256, resumable=True)
        body = {
                'name': sys.argv[2],
                'description': 'Big File',
                'mimeType': 'application/octet-stream'
        }

        retries = 0
        request = service.files().create(body=body, media_body=media_body)
        response = None
        while response is None:
                try:
                        status, response = request.next_chunk()
                        if status:
                                print ("Uploaded %.2f%%" % (status.progress() * 100))
                                retries = 0
                except errors.HttpError as e:
                        if e.resp.status == 404:
                                print ("Error 404! Aborting.")
                                exit()
                        else:   
                                if retries > 10:
                                        print ("Retries limit exceeded! Aborting.")
                                        exit()
                                else:   
                                        retries += 1
                                        time.sleep(2**retries)
                                        print ("Error (%d)... retrying." % e.resp.status)
                                        continue
        print ('Upload Complete, file ID: %s' % response.get('id'))

    # Download
    if sys.argv[1]== 'get':        
        file_id = sys.argv[2]
        request = service.files().get_media(fileId=file_id)
        filename = sys.argv[3]
        fh = io.FileIO(filename, 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print ('Download Complete, file path: ' + filename)

if __name__ == '__main__':
    main()
