pip install bs4 requests aiohttp datetime flask pandas sqlite-utils peewee pdfplumber python-dateutil

rm stylebook.db

sqlite-utils insert stylebook.db style_tips static/dbk_stylebook.csv --csv

python get_index.py

#to run, 'sh setup.sh'