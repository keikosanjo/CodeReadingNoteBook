#! /usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, request, jsonify, Response
from page_repository import PageRepository
import json
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
app.config['JSON_AS_ASCII'] = True

@app.route('/')
def test():
    return "hello world!"

#ページ取得API
@app.route('/pages',methods=['GET'])
def getall_pages():
    page_repository = PageRepository(access_point)
    pages = page_repository.getall()
    pages = pages.decode("utf-8")
    res = {'pages':[]}
    for page in pages:
        d = page.__dict__
        d['created_at'] = page.created_at.strftime('%Y-%m-%dT%H:%M:%S')
        d['updated_at'] = page.updated_at.strftime('%Y-%m-%dT%H:%M:%S')
        res['pages'].append(d)
    headers = {
        'content-type':'application/json'
    }
    return Response(response=json.dumps(str(res).decode("string-escape")), status=200, headers=headers)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
