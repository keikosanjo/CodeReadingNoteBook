# pageテーブルのorm
from  page_orm import Page
# mysql データベースへ接続
#from sqlalchemy import create_engine
from sqlalchemy import *
# セッション作成
from sqlalchemy.orm import sessionmaker
#from sqlalchemy.ext.declarative import declarative_base
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
import page_domain

class PageRepository():
    def __init__(self,url):
        # データベースへ接続
        engine = create_engine(url)
        #Base = declarative_base()
        #Base.metadata.bind=engine
        # セッション作成
        Session = sessionmaker(bind=engine)
        self.session = Session()

    #全件取得
    def getall(self):
        records = self.session.query(Page).all()
        pages = []
        for record in records:
            page = page_domain.Page(
                    id = record.id,
                    title = record.title,
                    relation_id = record.relation_id,
                    created_at = record.created_at,
                    updated_at = record.updated_at
                    )
            pages.append(page)
        return pages
        #self.session.close()

    #1件取得
    def get(self,id):
        page = self.session.query(Page).filter(Page.id==id)
        return page
