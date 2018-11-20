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
import belong_domain

class BelongRepository():
    def __init__(self,url):
        # データベースへ接続
        engine = create_engine(url)
        # セッション作成
        Session = sessionmaker(bind=engine)
        self.session = Session()

    #全belong取得(不要かも)
    def getall(self):
        records = self.session.query(Belong).all()
        belongs = []
        for record in records:
            belong = belong_domain.Belong(
                    id = record.id,
                    relation_order_00 = record.relation_order_00,
                    relation_order_01 = record.relation_order_01,
                    relation_order_02 = record.relation_order_02,
                    relation_order_03 = record.relation_order_03,
                    relation_order_04 = record.relation_order_04,
                    relation_order_05 = record.relation_order_05,
                    relation_order_06 = record.relation_order_06,
                    relation_order_07 = record.relation_order_07,
                    relation_order_08 = record.relation_order_08,
                    relation_order_09 = record.relation_order_09,
                    relation_order_10 = record.relation_order_10,
                    relation_order_11 = record.relation_order_11,
                    relation_order_12 = record.relation_order_12,
                    relation_order_13 = record.relation_order_13,
                    relation_order_14 = record.relation_order_14,
                    relation_order_15 = record.relation_order_15,
                    relation_order_16 = record.relation_order_16,
                    relation_order_17 = record.relation_order_17,
                    relation_order_18 = record.relation_order_18,
                    relation_order_19 = record.relation_order_19,
                    relation_order_20 = record.relation_order_20
                    )
            belongs.append(belong)
            print(belong.id)
            print(belong.relation_order_00)
            print(belong.relation_order_01)
            print(belong.relation_order_02)
        return belongs
        #self.session.close()

    #特定belong取得
    def get(self,belong_id):
        record = self.session.query(Belong).filter(Belong.id==belong_id).one()
        belong = belong_domain.Belong(
                    id = record.id,
                    relation_order_00 = record.relation_order_00,
                    relation_order_01 = record.relation_order_01,
                    relation_order_02 = record.relation_order_02,
                    relation_order_03 = record.relation_order_03,
                    relation_order_04 = record.relation_order_04,
                    relation_order_05 = record.relation_order_05,
                    relation_order_06 = record.relation_order_06,
                    relation_order_07 = record.relation_order_07,
                    relation_order_08 = record.relation_order_08,
                    relation_order_09 = record.relation_order_09,
                    relation_order_10 = record.relation_order_10,
                    relation_order_11 = record.relation_order_11,
                    relation_order_12 = record.relation_order_12,
                    relation_order_13 = record.relation_order_13,
                    relation_order_14 = record.relation_order_14,
                    relation_order_15 = record.relation_order_15,
                    relation_order_16 = record.relation_order_16,
                    relation_order_17 = record.relation_order_17,
                    relation_order_18 = record.relation_order_18,
                    relation_order_19 = record.relation_order_19,
                    relation_order_20 = record.relation_order_20
                )
        print(belong.id)
        print(belong.relation_order_00)
        print(belong.relation_order_01)
        print(belong.relation_order_02)
        return belong

    #belong登録
    def post(self, relation_order_00, relation_order_01, relation_order_02, relation_order_03, relation_order_04, relation_order_05, relation_order_06, relation_order_07, relation_order_08, relation_order_09, relation_order_10, relation_order_11, relation_order_12, relation_order_13, relation_order_14, relation_order_15, relation_order_16, relation_order_17, relation_order_18,relation_order_19, relation_order_20):
       belong = Belong(id=0, relation_order_00=relation_order_00, relation_order_01=relation_order_01, relation_order_02=relation_order_02, relation_order_03=relation_order_03, relation_order_04=relation_order_04, relation_order_05=relation_order_05, relation_order_06=relation_order_06, relation_order_07=relation_order_07, relation_order_08=relation_order_08, relation_order_09=relation_order_09, relation_order_10=relation_order_10, relation_order_11=relation_order_11, relation_order_12=relation_order_12, relation_order_13=relation_order_13, relation_order_14=relation_order_14, relation_order_15=relation_order_15, relation_order_16=relation_order_16, relation_order_17=relation_order_17, relation_order_18=relation_order_18, relation_order_19=relation_order_19, relation_order_20=relation_order_20)
       self.session.add(belong)
       self.session.commit()

    #特定ページ削除
    def delete(self, belong_id):
        belong = self.session.query(Belong).filter(Belong.id==belong_id).one()
        self.session.delete(belong)
        
    #ページ更新
    def put(self, belong_id, relation_order_00, relation_order_01, relation_order_02, relation_order_03, relation_order_04, relation_order_05, relation_order_06, relation_order_07, relation_order_08, relation_order_09, relation_order_10, relation_order_11, relation_order_12, relation_order_13, relation_order_14, relation_order_15, relation_order_16, relation_order_17, relation_order_18,relation_order_19, relation_order_20):
        belong = self.session.query(Belong).filter(Belong.id==belong_id).one()
        belong.relation_order_00 = relation_order_00
        belong.relation_order_01 = relation_order_01
        belong.relation_order_02 = relation_order_02
        belong.relation_order_03 = relation_order_03
        belong.relation_order_04 = relation_order_04
        belong.relation_order_05 = relation_order_05
        belong.relation_order_06 = relation_order_06
        belong.relation_order_07 = relation_order_07
        belong.relation_order_08 = relation_order_08
        belong.relation_order_09 = relation_order_09
        belong.relation_order_10 = relation_order_10
        belong.relation_order_11 = relation_order_11
        belong.relation_order_12 = relation_order_12
        belong.relation_order_13 = relation_order_13
        belong.relation_order_14 = relation_order_14
        belong.relation_order_15 = relation_order_15
        belong.relation_order_16 = relation_order_16
        belong.relation_order_17 = relation_order_17
        belong.relation_order_18 = relation_order_18
        belong.relation_order_19 = relation_order_19
        belong.relation_order_20 = relation_order_20
        self.session.commit()
        return belong

