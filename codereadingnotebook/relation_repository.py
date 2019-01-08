# 各テーブルのorm
from orm import *
# mysql データベースへ接続
from sqlalchemy import *
# セッション作成
from sqlalchemy.orm import sessionmaker
import relation_domain
from mysql_access_point import AccessPoint
get_access_point = AccessPoint()
access_point = get_access_point.end_point

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
