# データベースの設定
from sqlalchemy import create_engine
# データベースへ接続
from sqlalchemy.orm import sessionmaker
# クラス作成
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

# 接続するデータベース
engine = create_engine(access_point, echo=True)
# クラス作成
Base = declarative_base()

class Relation(Base):
    # マッピングするテーブル
    __tablename__ = 'relation'

    id = Column('relation_id', Integer, primary_key=True)
    code_link = Column('code_link', Text)
    memo = Column('memo', Text)
    created_at = Column(DateTime)
    update_at = Column(DateTime)
