import pandas as pd
from bs4 import BeautifulSoup
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
import json
import requests
import pdfplumber


###
# Google Authentication
###

# Load the Google service account JSON secret from an environment variable
#service_account_info = json.loads(os.environ['GOOGLE_SERVICE_SECRET'])

# Create a credentials object from the service account info
#creds = service_account.Credentials.from_service_account_info(service_account_info)

# Define the scopes that the application needs access to
#SCOPES = ['https://www.googleapis.com/auth/drive']

# Set up the Drive API client
#drive_service = build('drive', 'v3', credentials=creds)



###
# chat gpt example with one entry
###
# read the text file and split by lines
with open('file.txt', 'r') as f:
    lines = f.read().splitlines()

# create empty lists for name, description, and tag
name_list = []
description_list = []
tag_list = []

# loop through each line in the file and split by spaces
for line in lines:
    words = line.split()

    # if the line starts with "important", it is a new tag
    if words[0] == "important":
        tag = words[0]
        name = ""
        description = " ".join(words[1:])







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







