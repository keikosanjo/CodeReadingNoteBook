# mysql データベースへ接続
#from sqlalchemy import create_engine
from sqlalchemy import *
from sqlalchemy.orm import *
# テーブル生成&クラスマッピングに利用
from sqlalchemy.ext.declarative import declarative_base
# テーブル定義
from sqlalchemy import Column, Integer, ForeignKey, String, Text, DateTime
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

# データベースへ接続
engine = create_engine(access_point, echo=True)
# Baseクラス作成(クラス定義とテーブル紐づけ)
Base = declarative_base()

class Relation(Base):
    # マッピングするテーブル
    __tablename__ = 'relation'

    id = Column('id', Integer, primary_key=True)
    code_link = Column('code_link', Text)
    memo = Column('memo', Text)

class Belong(Base):
    # マッピングするテーブル
    __tablename__ = 'belong'

    id = Column('id', Integer, primary_key=True)
    relation_order_00 = Column('relation_order_00', Integer, ForeignKey('relation.id', onupdate="CASCASE", ondelete="CASCASE"))
    relation_order_01 = Column('relation_order_01', Integer, ForeignKey('relation.id', onupdate="CASCASE", ondelete="CASCASE"))
    relation_order_02 = Column('relation_order_02', Integer, ForeignKey('relation.id', onupdate="CASCASE", ondelete="CASCASE"))
    relation_order_03 = Column('relation_order_03', Integer, ForeignKey('relation.id', onupdate="CASCASE", ondelete="CASCASE"))
    relation_order_04 = Column('relation_order_04', Integer, ForeignKey('relation.id', onupdate="CASCASE", ondelete="CASCASE"))
    relation_order_05 = Column('relation_order_05', Integer, ForeignKey('relation.id', onupdate="CASCASE", ondelete="CASCASE"))
    relation_order_06 = Column('relation_order_06', Integer, ForeignKey('relation.id', onupdate="CASCASE", ondelete="CASCASE"))
    relation_order_07 = Column('relation_order_07', Integer, ForeignKey('relation.id', onupdate="CASCASE", ondelete="CASCASE"))
    relation_order_08 = Column('relation_order_08', Integer, ForeignKey('relation.id', onupdate="CASCASE", ondelete="CASCASE"))
    relation_order_09 = Column('relation_order_09', Integer, ForeignKey('relation.id', onupdate="CASCASE", ondelete="CASCASE"))
    relation_order_10 = Column('relation_order_10', Integer, ForeignKey('relation.id', onupdate="CASCASE", ondelete="CASCASE"))
    relation_order_11 = Column('relation_order_11', Integer, ForeignKey('relation.id', onupdate="CASCASE", ondelete="CASCASE"))
    relation_order_12 = Column('relation_order_12', Integer, ForeignKey('relation.id', onupdate="CASCASE", ondelete="CASCASE"))
    relation_order_13 = Column('relation_order_13', Integer, ForeignKey('relation.id', onupdate="CASCASE", ondelete="CASCASE"))
    relation_order_14 = Column('relation_order_14', Integer, ForeignKey('relation.id', onupdate="CASCASE", ondelete="CASCASE"))
    relation_order_15 = Column('relation_order_15', Integer, ForeignKey('relation.id', onupdate="CASCASE", ondelete="CASCASE"))
    relation_order_16 = Column('relation_order_16', Integer, ForeignKey('relation.id', onupdate="CASCASE", ondelete="CASCASE"))
    relation_order_17 = Column('relation_order_17', Integer, ForeignKey('relation.id', onupdate="CASCASE", ondelete="CASCASE"))
    relation_order_18 = Column('relation_order_18', Integer, ForeignKey('relation.id', onupdate="CASCASE", ondelete="CASCASE"))
    relation_order_19 = Column('relation_order_19', Integer, ForeignKey('relation.id', onupdate="CASCASE", ondelete="CASCASE"))
    relation_order_20 = Column('relation_order_20', Integer, ForeignKey('relation.id', onupdate="CASCASE", ondelete="CASCASE"))
    page = relationship('Page')

# 上で指定したクラスを作成
Base.metadata.create_all(engine)

class Page(Base):
    # マッピングするテーブル
    __tablename__ = 'page'

    id = Column('id', Integer, primary_key=True)
    title = Column('title', String(200))
    belong_id = Column('belong_id', Integer, ForeignKey('belong.id', onupdate="CASCASE", ondelete="CASCASE"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

# 上で指定したクラスを作成
Base.metadata.create_all(engine)
