# mysql データベースへ接続
#from sqlalchemy import create_engine
from sqlalchemy import *
from sqlalchemy.orm import *
# テーブル生成&クラスマッピングに利用
from sqlalchemy.ext.declarative import declarative_base
# テーブル定義
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
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

# データベースへ接続
engine = create_engine(access_point, echo=True)
# Baseクラス作成(クラス定義とテーブル紐づけ)
Base = declarative_base()

class Page(Base):
    # マッピングするテーブル
    __tablename__ = 'page'

    id = Column('page_id', Integer, primary_key=True)
    title = Column('title', String(200))
    belong_id = Column('belong_id', Integer, ForeignKey('belong.belong_id', onupdate="CASCASE", ondelete="CASCASE"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

# 上で指定したクラスを作成
Base.metadata.create_all(engine)
