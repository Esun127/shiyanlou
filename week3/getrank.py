#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from pymongo import MongoClient

def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests

    # 计算用户 user_id 的排名、总分数及花费的总时间
    TODO

    # 依次返回排名，分数和时间，不能修改顺序
    return rank, score, submit_time

if __name__ == '__main__':

    '''
    1. 判断参数格式是否符合要求
    '''
    if len(sys.argv) < 2:
        print('Usage: ./{} <user_id>'.format(sys.argv[0])
        sys.exit(-1)
    try:
        user_id = int(sys.argv[1])
    except ValueError as e:
        print(e)
        sys.exit(-1)

    '''
    2. 获取 user_id 参数
    '''
    TODO

    # 根据用户 ID 获取用户排名，分数和时间
    userdata = get_rank(user_id)
    print(userdata)
