from mongoengine import *
import pandas as pd
from tqdm import tqdm
import json
from datetime import datetime


connect(host="mongodb://rwuser:Qwer123-@120.46.142.25:8635/dianshang?authSource=admin")

def pre_process(o_d):
    if '+'==o_d[-1]:
        o_d = o_d[:-1]
    if '万' == o_d[-1]:
        o_d = int(float(o_d[:-1])*10000)
    return o_d

class Comment(EmbeddedDocument):
    star = IntField(required=True)
    nickname = StringField(required=True)
    isPlus = StringField(required=True)
    content = StringField(required=True)
    productType = StringField(required=True)
    time = StringField(required=True)
    month = IntField(required=True)
    quarter = IntField(required=True)

class Commodity(Document):
    keyword = StringField(required=True)
    skuId = StringField(required=True)
    title = StringField(required=True)
    price = FloatField(required=True)
    shop = StringField(required=True)
    sellCount = IntField(required=True)
    icon = StringField(required=True)
    firstClass = StringField(required=True)
    secondClass = StringField(required=True)
    commentList = ListField(EmbeddedDocumentField(Comment))

    meta = {
        'collections': 'commodity',
        'ordering': ['+skuId']
    }



class TestMongoEngine(object):
    def __init__(self):
        super(TestMongoEngine, self).__init__()
        pass

    def add_one(self, d):
        commentList = []
        mid_co = d['commentList'][2: -2].split('},{')
        for j in mid_co:
            j = json.loads('{'+j+'}')
            need_time = str(j['time'])
            mon = int(datetime.fromisoformat(need_time).month)
            qua = int((mon - 1) // 3 + 1)
            d_c = Comment(
                star = int(j['star']),
                nickname = str(j['nickname']),
                isPlus=str(j['isPlus']),
                content = str(j['content']),
                productType=str(j['productType']),
                time = need_time,
                month = mon,
                quarter = qua
            )
            commentList.append(d_c)

        p = d['productClass'].split('-')
        f = p[0]
        s = p[1]
        comd = Commodity(
            keyword = str(d['keyword']),
            skuId = str(d['skuId']),
            title = str(d['title']),
            price = float(d['price']),
            shop = str(d['shop']),
            sellCount = int(pre_process(o_d=d['sellCount'])),
            icon = str(d['icon']),
            firstClass = str(f),
            secondClass = str(s),
            commentList = commentList
        )
        comd.save()

def run():
    data = pd.read_csv('./all.csv')
    data_l = len(data)
    obj = TestMongoEngine()
    for i in tqdm(range(data_l)):
        try:
            obj.add_one(data.iloc[i])
        except:
            pass
        # obj.add_one(data.iloc[i])
if __name__ == '__main__':
    run()