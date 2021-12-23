from flask import Flask
from flask import jsonify
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask import request
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://rwuser:Qwer123-@120.46.142.25:8635/dianshang?authSource=admin&authMechanism=SCRAM-SHA-1'
}
app.config['SECRET_KEY'] = 'a random string'
app.config['JSON_AS_ASCII'] = False
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

db = MongoEngine(app)


class Comment(db.EmbeddedDocument):
    star = db.IntField(required=True)
    nickname = db.StringField(required=True)
    isPlus = db.StringField(required=True)
    content = db.StringField(required=True)
    productType = db.StringField(required=True)
    time = db.StringField(required=True)
    month = db.IntField(required=True)
    quarter = db.IntField(required=True)


class Commodity(db.Document):
    keyword = db.StringField(required=True)
    skuId = db.StringField(required=True)
    title = db.StringField(required=True)
    price = db.FloatField(required=True)
    shop = db.StringField(required=True)
    sellCount = db.IntField(required=True)
    icon = db.StringField(required=True)
    firstClass = db.StringField(required=True)
    secondClass = db.StringField(required=True)
    commentList = db.ListField(db.EmbeddedDocumentField(Comment))

    meta = {
        'collection': 'commodity',
        'ordering': ['+skuId']
    }


def construct_dict(cursor, cate):
    sc_dict = {}
    for i in cursor:
        sc_dict[i['_id']] = i[cate]
    return sc_dict


def construct_shopdict(cursor):
    sc_dict = {}
    for i in cursor:
        sc_dict[i['_id']] = int(i['count'])
    sc_dict = sorted(sc_dict.items(), key=lambda x: x[1], reverse=True)
    new_dict = []
    for k in range(10):
        new_dict.append({'no': k+1, 'name': str(sc_dict[k][0]), 'money': str(sc_dict[k][1])})
    # sc_dict = sc_dict[:10]
    return new_dict
    # r_d = {}
    # for j in sc_dict:
    #     r_d[j[0]] =j[1]
    # return r_d


def construct_mqdict(cl):
    time = {'month': [0,0,0,0,0,0,0,0,0,0,0,0],
        'quarter': [0,0,0,0]}
    for j in cl:
        for i in j.commentList:
            time['month'][int(i['month']-1)] += 1
            time['quarter'][int(i['quarter']-1)] += 1
    return time

def construct_stardict(cl):
    starall = {'star':  [0,0,0,0,0]}
    for j in cl:
        for i in j.commentList:
            starall['star'][i['star']-1] += 1
    return starall


@app.route('/api/v1/two', methods=['GET', 'POST'])
def gettwoclass():
    all_c = Commodity.objects.filter(firstClass='手机通讯').distinct("secondClass")
    all_json = {}
    avg = Commodity.objects.aggregate(
        [{"$match": {'firstClass': '手机通讯'}}, {'$group': {'_id': '$secondClass', 'avg': {'$avg': '$price'}}}])
    avg_dict = construct_dict(avg, 'avg')
    high = Commodity.objects.aggregate(
        [{"$match": {'firstClass': '手机通讯'}}, {'$group': {'_id': '$secondClass', 'max': {'$max': '$price'}}}])
    high_dict = construct_dict(high, 'max')
    min = Commodity.objects.aggregate(
        [{"$match": {'firstClass': '手机通讯'}}, {'$group': {'_id': '$secondClass', 'min': {'$min': '$price'}}}])
    min_dict = construct_dict(min, 'min')

    for i in range(len(all_c)):
        shop_name = all_c[i]
        count = Commodity.objects.filter(firstClass='手机通讯', secondClass=shop_name).count()
        mid = Commodity.objects.filter(firstClass='手机通讯').order_by('+price').skip(count // 2 + 1).limit(1).first().price
        s_c = {
            'avg': round(avg_dict[shop_name], 2),
            'mid': mid,
            'high': high_dict[shop_name],
            'min': min_dict[shop_name],
        }
        all_json[shop_name] = s_c
    return jsonify(all_json)


# @app.route("/api/v1/month", methods=["POST","GET"])
@app.route("/api/v1/time", methods=["POST", "GET"])
def getmonth():
    '''返回某个关键词的所有商品的季度和时间的数目'''

    # cursor = Commodity.objects.filter(skuId='10025617464281').all().commentList.aggregate([{'$group': {'_id': '$shop', 'count': {'$sum': 1}}}])
    skuId = request.args.get('Id')
    all = Commodity.objects.filter(skuId= skuId).all()
    all = construct_mqdict(all)
    return jsonify(all)
    # return jsonify({'month': [200, 233, 221, 323, 122, 212, 200, 233, 221, 323, 122, 212], 'title': 1223})

@app.route("/api/v1/hotshop", methods=["POST", "GET"])
def getshop():
    '''返回某一商品一级分类下销量前几名的热点店铺'''
    # all_s = Commodity.objects.filter(firstClass='手机通讯').distinct("shop")
    allcount = Commodity.objects.aggregate(
        [{"$match": {'firstClass': '手机通讯'}}, {'$group': {'_id': '$shop', 'count': {'$sum': '$sellCount'}}}])
    results = construct_shopdict(allcount)
    return jsonify(results)

@app.route("/api/v1/alldata", methods=["POST", "GET"])
def getall():
    skuId = request.args.get('Id')
    firstc = request.args.get('firstc')
    fc = Commodity.objects.filter(skuId= skuId).first().firstClass
    all = Commodity.objects.filter(skuId= skuId).all()
    total_dict = {}
    all_c = Commodity.objects.filter(firstClass=fc).distinct("secondClass")
    all_json = []
    avg = Commodity.objects.aggregate(
        [{"$match": {'firstClass': fc}}, {'$group': {'_id': '$secondClass', 'avg': {'$avg': '$price'}}}])
    avg_dict = construct_dict(avg, 'avg')
    high = Commodity.objects.aggregate(
        [{"$match": {'firstClass': fc}}, {'$group': {'_id': '$secondClass', 'max': {'$max': '$price'}}}])
    high_dict = construct_dict(high, 'max')
    min = Commodity.objects.aggregate(
        [{"$match": {'firstClass': fc}}, {'$group': {'_id': '$secondClass', 'min': {'$min': '$price'}}}])
    min_dict = construct_dict(min, 'min')

    for i in range(len(all_c)):
        shop_name = all_c[i]
        count = Commodity.objects.filter(firstClass=fc, secondClass=shop_name).count()
        mid = Commodity.objects.filter(firstClass=fc).order_by('+price').skip(count // 2 + 1).limit(1).first().price
        s_c = {
            'id': i+1,
            'name': shop_name,
            'avg': round(avg_dict[shop_name], 2),
            'mid': mid,
            'high': high_dict[shop_name],
            'min': min_dict[shop_name],
        }
        all_json.append(s_c)
    total_dict['two'] = all_json
    # -------------------------------------------------
    all_c1 = Commodity.objects.filter(firstClass=firstc).distinct("secondClass")
    all_json1 = []
    avg1 = Commodity.objects.aggregate(
        [{"$match": {'firstClass': firstc}}, {'$group': {'_id': '$secondClass', 'avg': {'$avg': '$price'}}}])
    avg_dict = construct_dict(avg1, 'avg')
    high1 = Commodity.objects.aggregate(
        [{"$match": {'firstClass': firstc}}, {'$group': {'_id': '$secondClass', 'max': {'$max': '$price'}}}])
    high_dict = construct_dict(high1, 'max')
    min1 = Commodity.objects.aggregate(
        [{"$match": {'firstClass': firstc}}, {'$group': {'_id': '$secondClass', 'min': {'$min': '$price'}}}])
    min_dict = construct_dict(min1, 'min')

    for i in range(len(all_c1)):
        shop_name = all_c1[i]
        count = Commodity.objects.filter(firstClass=firstc, secondClass=shop_name).count()
        mid = Commodity.objects.filter(firstClass=firstc).order_by('+price').skip(count // 2 + 1).limit(1).first().price
        s_c = {
            'id': i + 1,
            'name': shop_name,
            'avg': round(avg_dict[shop_name], 2),
            'mid': mid,
            'high': high_dict[shop_name],
            'min': min_dict[shop_name],
        }
        all_json.append(s_c)
    total_dict['sc'] = all_json1

    # ----------------------------------
    all1 = construct_mqdict(all)
    total_dict['time'] = all1
    # ----------------------------------------------
    allcount = Commodity.objects.aggregate(
        [{"$match": {'firstClass': fc}}, {'$group': {'_id': '$shop', 'count': {'$sum': '$sellCount'}}}])
    results = construct_shopdict(allcount)
    total_dict['shop'] = results
    # -----------------------------------------
    all2 = construct_stardict(all)
    star_dict = all2['star']
    total_dict['category'] = {'data1': star_dict, 'axisX': ['一星评价','二星评价','三星评价','四星评价','五星评价']}
    return jsonify(total_dict)


if __name__ == '__main__':
    app.run(debug=True)
