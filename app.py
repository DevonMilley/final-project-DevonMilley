import pandas as pd
from bs4 import BeautifulSoup
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
import json
import requests
from flask import Flask, render_template, request, flash, redirect, url_for
from playhouse.sqlite_ext import *
from peewee import *

app = Flask(__name__)
#app.secret_key = "279878dhekdhkhekdhkh" #can i use the same api key for this

db = SqliteExtDatabase('stylebook.db')


class Stylebook(Model):
    id = IntegerField(unique=True)
    name = CharField()
    description = TextField()
    tags = CharField()

    class Meta:
        table_name = "style_tips"
        database = db

class StylebookIndex(FTSModel):
    rowid = RowIDField()
    description = SearchField()

    class Meta:
        database = db
        options = {'tokenize': 'porter', 'content': Stylebook.description}


@app.route("/open_index", methods=['GET', 'POST'])
def open_index():
    all_tips = Stylebook.select()
    results = None
    search_term = None
    document_count = Stylebook.select().count()
    recent = Stylebook.select().get()
    return render_template('index.html', all_tips=all_tips, results=results, document_count=document_count, search_term=search_term, recent=recent)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_term = request.form['search_term']
        results = (Stylebook.select(Stylebook, StylebookIndex.rank()).join(StylebookIndex,on=(Stylebook.id == StylebookIndex.rowid)).where(StylebookIndex.match(search_term)).order_by(Stylebook.name))
        document_count = len(list(set([x for x in results])))
        if document_count > 0:
            recent = results.get()
        else:
            recent = Stylebook.select().get()
    else:
        results = None
        search_term = None
        document_count = Stylebook.select().count()
        recent = Stylebook.select().get()
    all_tips = Stylebook.select()
    return render_template('index.html', all_tips = all_tips, results = results, document_count=document_count, search_term = search_term, recent=recent)

@app.route("/open_important", methods=['GET', 'POST'])
def open_important():
    all_tips = Stylebook.select()
    results = None
    search_term = None
    document_count = Stylebook.select().count()
    recent = Stylebook.select().get()
    return render_template('important.html', all_tips=all_tips, results=results, document_count=document_count, search_term=search_term, recent=recent)

@app.route("/important", methods=['GET', 'POST'])
def important():
    if request.method == 'POST':
        search_term = request.form['search_term']
        results = (Stylebook.select(Stylebook, StylebookIndex.rank()).join(StylebookIndex,on=(Stylebook.id == StylebookIndex.rowid)).where(StylebookIndex.match(search_term)).order_by(Stylebook.name))
        document_count = len(list(set([x for x in results])))
        if document_count > 0:
            recent = results.get()
        else:
            recent = Stylebook.select().get()
    else:
        results = None
        search_term = None
        document_count = Stylebook.select().count()
        recent = Stylebook.select().get()
    all_tips = Stylebook.select()
    return render_template('important.html', all_tips=all_tips, results=results, document_count=document_count, search_term=search_term, recent=recent)

@app.route("/open_ap_dev", methods=['GET', 'POST'])
def open_ap_dev():
    all_tips = Stylebook.select()
    results = None
    search_term = None
    document_count = Stylebook.select().count()
    recent = Stylebook.select().get()
    return render_template('ap_dev.html', all_tips=all_tips, results=results, document_count=document_count, search_term=search_term, recent=recent)

@app.route("/ap_dev", methods=['GET', 'POST'])
def ap_dev():
    if request.method == 'POST':
        search_term = request.form['search_term']
        results = (Stylebook.select(Stylebook, StylebookIndex.rank()).join(StylebookIndex,on=(Stylebook.id == StylebookIndex.rowid)).where(StylebookIndex.match(search_term)).order_by(Stylebook.name))
        document_count = len(list(set([x for x in results])))
        if document_count > 0:
            recent = results.get()
        else:
            recent = Stylebook.select().get()
    else:
        results = None
        search_term = None
        document_count = Stylebook.select().count()
        recent = Stylebook.select().get()
    all_tips = Stylebook.select()
    return render_template('ap_dev.html', all_tips=all_tips, results=results, document_count=document_count, search_term=search_term, recent=recent)

@app.route("/open_sports", methods=['GET', 'POST'])
def open_sports():
    all_tips = Stylebook.select()
    results = None
    search_term = None
    document_count = Stylebook.select().count()
    recent = Stylebook.select().get()
    return render_template('sports.html', all_tips=all_tips, results=results, document_count=document_count, search_term=search_term, recent=recent)

@app.route("/sports", methods=['GET', 'POST'])
def sports():
    if request.method == 'POST':
        search_term = request.form['search_term']
        results = (Stylebook.select(Stylebook, StylebookIndex.rank()).join(StylebookIndex,on=(Stylebook.id == StylebookIndex.rowid)).where(StylebookIndex.match(search_term)).order_by(Stylebook.name))
        document_count = len(list(set([x for x in results])))
        if document_count > 0:
            recent = results.get()
        else:
            recent = Stylebook.select().get()
    else:
        results = None
        search_term = None
        document_count = Stylebook.select().count()
        recent = Stylebook.select().get()
    all_tips = Stylebook.select()
    return render_template('sports.html', all_tips=all_tips, results=results, document_count=document_count, search_term=search_term, recent=recent)


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




