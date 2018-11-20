from flask import Flask, request
from page_repository import PageRepository
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

app = Flask(__name__)

@app.route('/')
def test():
    return "hello world!"

#ページ取得API
@app.route('/pages')
def getall_pages():
    page_repository = PageRepository(access_point)
    pages = []
    pages = page_repository.getall()
    return pages
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
