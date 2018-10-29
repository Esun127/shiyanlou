#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from pymongo import MongoClient
import pymongo


def rank_score(doc):
    return doc['score']



def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests

    ranks = []
    #r = contests.create_index(['user_id', pymongo.ASCENDING], unique=True)
    #if r:
    for d in contests.find().sort('user_id'):
        score = 0
        submit_time = 0
        userid = d.get('user_id')
        tmp = {}
        for dd in contests.find({'user_id':userid}):
            score += dd.get('score')
            submit_time += dd.get('submit_time')
        tmp['user_id'] = userid
        tmp['score'] = score
        tmp['submit_time'] = submit_time
        if tmp not in ranks:
            ranks.append({ 'user_id':userid,'score':score,'submit_time':submit_time})

    
    ranks = sorted(ranks, key=rank_score, reverse=True)
    #print(ranks)

    for i in ranks:
        n = ranks.index(i)
        for j in ranks[n+1:]:
            if i.get('score') == j.get('score')  and i.get('submit_time') > j.get('submit_time'):
                m = ranks.index(j)
                ranks[n], ranks[m] = j, i
    
    for i, j  in enumerate(ranks):
        if j.get('user_id') == user_id:
            return i+1, j.get('score'), j.get('submit_time')


    
    # 计算用户 user_id 的排名、总分数及花费的总时间
    #TODO

    # 依次返回排名，分数和时间，不能修改顺序
    #return rank, score, submit_time

if __name__ == '__main__':

    '''
    1. 判断参数格式是否符合要求
    '''
    if len(sys.argv) < 2:
        print('Parameter Error')
        print('Usage: ./{} <user_id>'.format(sys.argv[0]))
        sys.exit(-1)
    try:
        user_id = int(sys.argv[1])
    except ValueError as e:
        print('Parameter Error')
        sys.exit(-2)

    '''
    2. 获取 user_id 参数
    '''
    #TODO

    # 根据用户 ID 获取用户排名，分数和时间
    userdata = get_rank(user_id)
    print(userdata)

