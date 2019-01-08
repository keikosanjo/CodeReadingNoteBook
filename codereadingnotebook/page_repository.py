# 各テーブルのorm
from orm import *
# mysql データベースへ接続
from sqlalchemy import *
# セッション作成
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import page_domain
from mysql_access_point import AccessPoint
get_access_point = AccessPoint()
access_point = get_access_point.end_point

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
        self.session.commit()
        
    #ページ更新
    def put(self,page_id,title):
        now_time = datetime.now()
        page = self.session.query(Page).filter(Page.id==page_id).one()
        page.title = title
        page.updated_at = now_time
        self.session.commit()
        return page
