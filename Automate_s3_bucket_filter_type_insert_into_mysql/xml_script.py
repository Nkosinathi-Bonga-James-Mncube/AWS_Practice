from datetime import time
import sys
import xml.etree.ElementTree as data1
import pandas as pd
import sqlalchemy as db
from sqlalchemy import Integer,Text,String,MetaData,Table,Column
from sqlalchemy.sql.expression import text
from sqlalchemy_utils import database_exists,create_database
import pymysql

engine = db.create_engine('mysql+pymysql://root:{{password}}@0.0.0.0:3306/test_database' )
if not database_exists(engine.url):
        create_database(engine.url)        
connection = engine.connect()
metadata = db.MetaData()
test1 = Table(sys.argv[2], metadata,
db.Column('entry',db.Integer,primary_key=True),
db.Column('name',db.Text(1000),nullable=True),
db.Column('surname',db.Text(1000),nullable=False),
)
csv_file_example = open(sys.argv[1], "r");

metadata.create_all(engine)
data_c = pd.read_csv(csv_file_example);
database_csv = pd.DataFrame(data_c)
# 
database_csv.to_sql(
 name=sys.argv[2],
 con = engine,
 if_exists = 'append',
 chunksize = 500,
 index = False,
 dtype={
          
        "name" : Text,
        "surname": Text,
 }
)
# 