import pandas as pd
from bs4 import BeautifulSoup
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
import json
import requests
from flask import Flask
from flask import render_template
from peewee import *

app = Flask(__name__)
#app.secret_key = "279878dhekdhkhekdhkh" #can i use the same api key for this
#db = SqliteDatabase('foreclosures.db')

db = SqliteDatabase('stylebook.db')


class Stylebook(Model):
    id = IntegerField(unique=True)
    name = CharField()
    description = CharField()
    tags = CharField()

    class Meta:
        table_name = "style_tips"
        database = db

@app.route("/")
def index():
    all_tips = Stylebook.select()
    template = 'index.html'
    return render_template(template, all_tips = all_tips)





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

# Read dbk_stylebook csv
#csv_data = pd.read_csv('dbk_stylebook.csv')






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


if __name__ == '__main__':
   app.run(debug=True, use_reloader=True)




