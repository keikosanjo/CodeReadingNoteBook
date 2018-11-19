# 各テーブルのorm
from orm import *
# mysql データベースへ接続
#from sqlalchemy import create_engine
from sqlalchemy import *
# セッション作成
from sqlalchemy.orm import sessionmaker
from datetime import datetime
# 機密情報外出し
import configparser
config = configparser.ConfigParser()
config.read('../config.py')
user_name = config['DATABASE']['Username']
password = config['DATABASE']['Password']
endpoint = config['DATABASE']['Endpoint']
port = config['DATABASE']['Port']
database_name = config['DATABASE']['Databasename']
access_point = 'mysql://' + user_name + ':' + password + '@' + endpoint + ':' + port + '/' + database_name + '?charset=utf8'
import page_domain

class PageRepository():
    def __init__(self,url):
        # データベースへ接続
        engine = create_engine(url)
        # セッション作成
        Session = sessionmaker(bind=engine)
        self.session = Session()

    #全ページ取得
    def getall(self):
        records = self.session.query(Page).all()
        pages = []
        for record in records:
            page = page_domain.Page(
                    id = record.id,
                    title = record.title,
                    belong_id = record.belong_id,
                    created_at = record.created_at,
                    updated_at = record.updated_at
                    )
            pages.append(page)
            print(page.id)
            print(page.title)
            print(page.belong_id)
            print(page.created_at)
            print(page.updated_at)
        return pages
        #self.session.close()

    #特定ページ取得
    def get(self,page_id):
        record = self.session.query(Page).filter(Page.id==page_id).one()
        page = page_domain.Page(
                id = record.id,
                title = record.title,
                belong_id = record.belong_id,
                created_at = record.created_at,
                updated_at = record.updated_at
                )
        return page

    #ページ登録
    def post(self,title,belong_id):
       now_time = datetime.now()
       page = Page(id=0, title=title, belong_id=belong_id, created_at=now_time, updated_at=now_time)
       self.session.add(page)
       self.session.commit()

    #特定ページ削除
    def delete(self, page_id):
        page = self.session.query(Page).filter(Page.id==page_id).one()
        self.session.delete(page)
        
    #ページ更新
    def put(self,page_id,title):
        now_time = datetime.now()
        page = self.session.query(Page).filter(Page.id==page_id).one()
        page.title = title
        page.updated_at = now_time
        self.session.commit()
        return page
