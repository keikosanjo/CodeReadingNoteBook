# pageテーブルのorm
import page_orm
# mysql データベースの設定
from sqlalchemy import create_engine
# mysql データベースに接続
from sqlalchemy.orm import sessionmaker
# 機密情報外出し
import configparser
config = configparser.ConfigParser()
config.read('../config.py')
user_name = config['DATABASE']['Username']
password = config['DATABASE']['Password']
endpoint = config['DATABASE']['Endpoint']
port = config['DATABASE']['Port']
database_name = config['DATABASE']['Databasename']
access_point = 'mysql://' + user_name + ':' + password + '@' + endpoint + ':' + port + '/' + database_name

class PageRepository():
    def __init__(self):
        engine = create_engine(access_point)
        Session = sessionmaker(bind=engine)
        session = Session()

    def save(self):
