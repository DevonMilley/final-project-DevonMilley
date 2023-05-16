pip install google-api-python-client bs4 requests google-auth google-auth-oauthlib google-auth-httplib2 aiohttp datetime flask pandas sqlite-utils peewee pdfplumber python-dateutil

rm stylebook.db

sqlite-utils insert stylebook.db style_tips static/dbk_stylebook.csv --csv

#to run, 'sh setup.sh'