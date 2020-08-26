import mysql.connector
import os
print(os.environ)
linkdb = mysql.connector.connect(
  host=os.getenv('HOST'),
  user=os.getenv('USER'),
  password=os.getenv('PASSWORD'),
  database=os.getenv('DATABASE','zyrkxxxs_shortener')
)

def add_data(long,short):
  cursor = linkdb.cursor()
  try:
    cursor.execute("INSERT INTO links (link, shortlink) VALUES( %s, %s)",(long, short))
    linkdb.commit()
    return 'short url created!'
  except(mysql.connector.errors.IntegrityError):
    return 'BHAI BANCHUKA YE'

def find_url(short):
  cursor = linkdb.cursor()
  try:
    cursor.execute("select * from links where shortlink ='{}'".format(short))
    linkrow= cursor.fetchone()
    return linkrow[1]
  except:
    return 'LINK NOT FOUND SORRI'
