from pymongo import MongoClient
import time
import hashlib
import re


def insert_mongo(db, collections, data):
    try:
        result = collections.insert(data)
        print('enter' + str(result) + str(data))
    exec 


class DataModels:

    def __init__(self):
        self.client = MongoClient('mongodb://admin:test@116.62.144.245:27017/')
        self.db = self.client.admin

    # 持久化微博热搜
    def save_weibo(self, title, url, hot):
        if re.match('http', url) is None:
            return
        weibo_item = {
            'title': title,
            'url': url,
            'hot': hot,
            'url_md5': hashlib.md5(url.encode(encoding='UTF-8')).hexdigest(),
            'create_time': time.time()
        }
        insert_mongo(self.db.weibo, weibo_item)

    def save_wexin(self):
        print(self)
