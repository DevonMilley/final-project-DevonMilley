import pandas as pd
from bs4 import BeautifulSoup
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
import json
import requests
import logging

logging.basicConfig(level=logging.DEBUG)


###
# Google Authentication
###

# Define the path to the service account JSON file
#SERVICE_ACCOUNT_FILE = os.environ.get('GOOGLE_SERVICE')
#creds_dict = json.loads(SERVICE_ACCOUNT_FILE)
#creds = service_account.Credentials.from_service_account_info(creds_dict)

# Load the Google service account JSON secret from an environment variable
service_account_info = json.loads(os.environ['GOOGLE_SERVICE_SECRET'])

# Create a credentials object from the service account info
creds = service_account.Credentials.from_service_account_info(service_account_info)

# Define the scopes that the application needs access to
SCOPES = ['https://www.googleapis.com/auth/drive']

# Set up the Drive API client
drive_service = build('drive', 'v3', credentials=creds)

###
# Getting the PDF
###

with open('2022 DBK Stylebook.html', 'r') as f:
    html_text = f.read()

pdf_soup = BeautifulSoup(html_text, 'html.parser')

b_tag = pdf_soup.find_all("p", {"class": "s10"})

print(b_tag)


###
# Grab Google Doc information and manipulate
###

# Retrieve the content of the Google Doc in HTML format
# file_id = '1wBtEXq3LsxVOjqMT0RoEoQxbJShfPu1H2M0gLsJOOY8'
# export_mime_type = 'text/html'
# response = drive_service.files().export(fileId=file_id, mimeType=export_mime_type).execute()

# # Extract the HTML content from the API response
# doc_content = response.decode('utf-8')

# # Parse the HTML content using Beautiful Soup
# soup = BeautifulSoup(doc_content, 'html.parser')







