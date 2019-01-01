# 各テーブルのorm
from orm import *
# mysql データベースへ接続
from sqlalchemy import *
# セッション作成
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
access_point = 'mysql://' + user_name + ':' + password + '@' + endpoint + ':' + port + '/' + database_name + '?charset=utf8'
import relation_domain

class RelationRepository():
    def __init__(self,url):
        # データベースへ接続
        engine = create_engine(url)
        # セッション作成
        Session = sessionmaker(bind=engine)
        self.session = Session()

    #全relation取得
    def getall(self):
        records = self.session.query(Relation).all()
        relations = []
        for record in records:
            relation = relation_domain.Relation(
                    id = record.id,
                    code_link = record.code_link,
                    memo = record.memo
                    )
            relations.append(relation)
        return relations
        #self.session.close()

    #特定relation取得
    def get(self,relation_id):
        record = self.session.query(Relation).filter(Relation.id==relation_id).one()
        relation = relation_domain.Relation(
                    id = record.id,
                    code_link = record.code_link,
                    memo = record.memo
                    )
        return relation

    #relation登録
    def post(self, code_link, memo):
       relation = Relation(id=0, code_link=code_link, memo=memo)
       self.session.add(relation)
       self.session.commit()

    #特定relation削除
    def delete(self, relation_id):
        relation = self.session.query(Relation).filter(Relation.id==relation_id).one()
        self.session.delete(relation)
        self.session.commit()
        
    #relation更新
    def put(self, relation_id, code_link, memo):
        relation = self.session.query(Relation).filter(Relation.id==relation_id).one()
        relation.code_link = code_link
        relation.memo = memo
        self.session.commit()
        return relation
