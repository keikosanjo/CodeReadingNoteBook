#! /usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, jsonify, request
from page_repository import PageRepository
from belong_repository import BelongRepository
from relation_repository import RelationRepository
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

################
##  page関連  ##
################

#全ページ取得API
@app.route('/pages',methods=['GET'])
def getall_pages():
    page_repository = PageRepository(access_point)
    pages = page_repository.getall()
    res = {'pages':[]}
    for page in pages:
        d = page.__dict__
        d['created_at'] = page.created_at.strftime('%Y-%m-%dT%H:%M:%S')
        d['updated_at'] = page.updated_at.strftime('%Y-%m-%dT%H:%M:%S')
        res['pages'].append(d)
    return jsonify(res),200 

#特定ページ取得API
@app.route('/pages/<page_id>',methods=['GET'])
def get_page(page_id):
    page_repository = PageRepository(access_point)
    page = page_repository.get(page_id)
    res = {'page':[]}
    d = page.__dict__
    d['created_at'] = page.created_at.strftime('%Y-%m-%dT%H:%M:%S')
    d['updated_at'] = page.updated_at.strftime('%Y-%m-%dT%H:%M:%S')
    res['page'].append(d)
    return jsonify(res),200

#ページ作成API
@app.route('/pages',methods=['POST'])
def post_page():
    title = request.args.get('title','')
    belong_id = request.args.get('belong_id','')
    page_repository = PageRepository(access_point)
    page = page_repository.post(title,belong_id)
    return request.data

#特定ページ削除API
@app.route('/pages/<page_id>', methods=['DELETE'])
def delete_page(page_id):
    page_repository = PageRepository(access_point)
    page = page_repository.delete(page_id)
    return jsonify({'status':'OK'})

#ページ更新API
@app.route('/pages/<page_id>', methods=['PUT'])
def put_page(page_id):
    page_repository = PageRepository(access_point)
    page = page_repository.get(page_id)
    if request.values.get('title') is not None:
        title = request.values.get('title')
    else:
        title = page.title
    page = page_repository.put(page_id,title)
    return request.data

#################
## belong関連  ##
#################

numbers = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]

#全belong取得API
@app.route('/belongs',methods=['GET'])
def getall_belongs():
    belong_repository = BelongRepository(access_point)
    belongs = belong_repository.getall()
    res = {'belongs':[]}
    for belong in belongs:
        d = belong.__dict__
        res['belongs'].append(d)
    return jsonify(res),200 

#特定belong取得API
@app.route('/belongs/<belong_id>',methods=['GET'])
def get_belong(belong_id):
    belong_repository = BelongRepository(access_point)
    belong = belong_repository.get(belong_id)
    res = {'belong':[]}
    d = belong.__dict__
    res['belong'].append(d)
    return jsonify(res),200

#belong作成API
@app.route('/belongs',methods=['POST'])
def post_belong():
    for i in numbers:
        globals()["relation_order_" + str(i)] = request.args.get('relation_order_%s'%i)
    belong_repository = BelongRepository(access_point)
    belong = belong_repository.post(relation_order_00, relation_order_01, relation_order_02, relation_order_03, relation_order_04, relation_order_05, relation_order_06, relation_order_07, relation_order_08, relation_order_09, relation_order_10, relation_order_11, relation_order_12, relation_order_13, relation_order_14, relation_order_15, relation_order_16, relation_order_17, relation_order_18, relation_order_19, relation_order_20)
    return request.data

#特定belong削除API
@app.route('/belongs/<belong_id>', methods=['DELETE'])
def delete_belong(belong_id):
    belong_repository = BelongRepository(access_point)
    belong = belong_repository.delete(belong_id)
    return jsonify({'status':'OK'})

#belong更新API
@app.route('/belongs/<belong_id>', methods=['PUT'])
def put_belong(belong_id):
    belong_repository = BelongRepository(access_point)
    belong = belong_repository.get(belong_id)
    if request.values.get('relation_order_00') is not None:
        relation_order_00 = request.values.get('relation_order_00')
    else:
        relation_order_00 = belong.relation_order_00
    if request.values.get('relation_order_01') is not None:
        relation_order_01 = request.values.get('relation_order_01')
    else:
        relation_order_01 = belong.relation_order_01
    if request.values.get('relation_order_02') is not None:
        relation_order_02 = request.values.get('relation_order_02')
    else:
        relation_order_02 = belong.relation_order_02
    if request.values.get('relation_order_03') is not None:
        relation_order_03 = request.values.get('relation_order_03')
    else:
        relation_order_03 = belong.relation_order_03
    if request.values.get('relation_order_04') is not None:
        relation_order_04 = request.values.get('relation_order_04')
    else:
        relation_order_04 = belong.relation_order_04
    if request.values.get('relation_order_05') is not None:
        relation_order_05 = request.values.get('relation_order_05')
    else:
        relation_order_05 = belong.relation_order_05
    if request.values.get('relation_order_06') is not None:
        relation_order_06 = request.values.get('relation_order_06')
    else:
        relation_order_06 = belong.relation_order_06
    if request.values.get('relation_order_07') is not None:
        relation_order_07 = request.values.get('relation_order_07')
    else:
        relation_order_07 = belong.relation_order_07
    if request.values.get('relation_order_08') is not None:
        relation_order_08 = request.values.get('relation_order_08')
    else:
        relation_order_08 = belong.relation_order_08
    if request.values.get('relation_order_09') is not None:
        relation_order_09 = request.values.get('relation_order_09')
    else:
        relation_order_09 = belong.relation_order_09
    if request.values.get('relation_order_10') is not None:
        relation_order_10 = request.values.get('relation_order_10')
    else:
        relation_order_10 = belong.relation_order_10
    if request.values.get('relation_order_11') is not None:
        relation_order_11 = request.values.get('relation_order_11')
    else:
        relation_order_11 = belong.relation_order_11
    if request.values.get('relation_order_12') is not None:
        relation_order_12 = request.values.get('relation_order_12')
    else:
        relation_order_12 = belong.relation_order_12
    if request.values.get('relation_order_13') is not None:
        relation_order_13 = request.values.get('relation_order_13')
    else:
        relation_order_13 = belong.relation_order_13
    if request.values.get('relation_order_14') is not None:
        relation_order_14 = request.values.get('relation_order_14')
    else:
        relation_order_14 = belong.relation_order_14
    if request.values.get('relation_order_15') is not None:
        relation_order_15 = request.values.get('relation_order_15')
    else:
        relation_order_15 = belong.relation_order_15
    if request.values.get('relation_order_16') is not None:
        relation_order_16 = request.values.get('relation_order_16')
    else:
        relation_order_16 = belong.relation_order_16
    if request.values.get('relation_order_17') is not None:
        relation_order_17 = request.values.get('relation_order_17')
    else:
        relation_order_17 = belong.relation_order_17
    if request.values.get('relation_order_18') is not None:
        relation_order_18 = request.values.get('relation_order_18')
    else:
        relation_order_18 = belong.relation_order_18
    if request.values.get('relation_order_19') is not None:
        relation_order_19 = request.values.get('relation_order_19')
    else:
        relation_order_19 = belong.relation_order_19
    if request.values.get('relation_order_20') is not None:
        relation_order_20 = request.values.get('relation_order_20')
    else:
        relation_order_20 = belong.relation_order_20
    belong = belong_repository.put(belong_id, relation_order_00, relation_order_01, relation_order_02, relation_order_03, relation_order_04, relation_order_05, relation_order_06, relation_order_07, relation_order_08, relation_order_09, relation_order_10, relation_order_11, relation_order_12, relation_order_13, relation_order_14, relation_order_15, relation_order_16, relation_order_17, relation_order_18, relation_order_19, relation_order_20)
    return request.data

####################
##  relation関連  ##
####################

#全relation取得API
@app.route('/relations',methods=['GET'])
def getall_relations():
    relation_repository = RelationRepository(access_point)
    relations = relation_repository.getall()
    res = {'relations':[]}
    for relation in relations:
        d = relation.__dict__
        res['relations'].append(d)
    return jsonify(res),200 

#特定relation取得API
@app.route('/relations/<relation_id>',methods=['GET'])
def get_relation(relation_id):
    relation_repository = RelationRepository(access_point)
    relation = relation_repository.get(relation_id)
    res = {'relation':[]}
    d = relation.__dict__
    res['relation'].append(d)
    return jsonify(res),200

#relation作成API
@app.route('/relations',methods=['POST'])
def post_relation():
    code_link = request.args.get('code_link','')
    memo = request.args.get('memo','')
    relation_repository = RelationRepository(access_point)
    relation = relation_repository.post(code_link,memo)
    return request.data

#特定relation削除API
@app.route('/relations/<relation_id>', methods=['DELETE'])
def delete_relation(relation_id):
    relation_repository = RelationRepository(access_point)
    relation = relation_repository.delete(relation_id)
    return jsonify({'status':'OK'})

#relation更新API
@app.route('/relations/<relation_id>', methods=['PUT'])
def put_relation(relation_id):
    relation_repository = RelationRepository(access_point)
    relation = relation_repository.get(relation_id)
    if request.values.get('code_link') is not None:
        code_link = request.values.get('code_link')
    else:
        code_link = relation.code_link
    if request.values.get('memo') is not None:
        memo = request.values.get('memo')
    else:
        memo = relation.memo
    relation = relation_repository.put(relation_id,code_link,memo)
    return request.data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
