from flask import Flask, abort
from flask_mongoengine import MongoEngine

app = Flask(__name__)
# 只有这种方法才能授权成功其它都失败
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://rwuser:Qwer123-@120.46.142.25:8635/student?authSource=admin&authMechanism=SCRAM-SHA-1'
}
app.config['SECRET_KEY'] = 'a random string'
db = MongoEngine(app)

class Grade(db.EmbeddedDocument):
    name = db.StringField(required=True)
    score = db.FloatField(required=True)

SEX_CHOICE = (
    ('male', '男'),
    ('female', '女')
)

# 上面coonect 连接的是数据库 后面连接的是collections 没有指定集合的话就是collection这个集合
class Student(db.Document):
    name = db.StringField(max_length=32, required=True)
    age = db.IntField(required=True)
    sex = db.StringField(choices=SEX_CHOICE, required=True)
    grade = db.StringField()
    address = db.StringField()
    grades = db.ListField(db.EmbeddedDocumentField(Grade))

    # 配置元数据，设置 设置集合的名字。
    meta = {
        'collection': 'student',
        'ordering': ['-age']
    }

@app.route('/')
def index():
    # abort(404)
    a = (Student.objects.filter(name='王豫').first().age)
    return str(a)

if __name__ == '__main__':
    app.run(debug=True)