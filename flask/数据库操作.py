from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId


class TestMongo(object):
    def __init__(self):
        self.client = MongoClient('mongodb://rwuser:Qwer123-@120.46.142.25:8635/')
        self.db = self.client['imooc']

    def add_one(self):
        '''添加一条数据'''
        post = {
            'title':'斗破',
            'content': '1212传送倒数第三21212个3',
            'price': 10,
            'created_at': datetime.now()
        }
        return self.db.imooc.post.insert_one(post)

    def query_one(self):
        '''查询一条数据'''
        return self.db.imooc.post.find_one()

    def query_all(self):
        # 返回全部数据
        return self.db.imooc.post.find({'title': '三体'})

    def query_byid(self, id):
        '''按照id查询'''
        id = ObjectId(id)
        return self.db.imooc.post.find_one({"_id": id})

    def update(self):
        # 更新一条数据
        # rest = self.db.imooc.post.update_one({}, {'$inc'：price+100})
        #     更新对应的数据 返回符合条件和修改的数目
        rest = self.db.imooc.post.update_many({'title': '斗破'}, {'$inc': {'price':100}})
        # print(rest.matched_count)
        # print(rest.modified_count)
        return rest

    def delete(self):
        # 删除数据
    #     删除一条数据
    #     rest = self.db.imooc.post.delete_one({'title': '斗破'})
        rest = self.db.imooc.post.delete_many({'title': '斗破'})
        # print(rest.deleted_count)
        return rest

    def close(self):
        # 关闭连接
        self.client.close()



def run():
    obj = TestMongo()
    # print(obj.add_one())
    # print(obj.query_one())
    # obj.update()
    obj.delete()
    # mul = obj.query_all()
    # for i in mul:
    #     print(i)
    # z = obj.query_byid('61a043ff0274c1b776c2d620')
    # print(z)
    # for j in z:
    #     print(j)

if __name__ == '__main__':
    run()