from mongoengine import *

# connect, Document, StringField, IntField, EmbeddedDocument, FloatField, EmbeddedDocumentField, \
# ListField


# 创建学生数据库
connect(host='mongodb://rwuser:Qwer123-@120.46.142.25:8635/student?authSource=admin')


class Grade(EmbeddedDocument):
    name = StringField(required=True)
    score = FloatField(required=True)


SEX_CHOICE = (
    ('male', '男'),
    ('female', '女')
)

# 上面coonect 连接的是数据库 后面连接的是collections 没有指定集合的话就是collection这个集合
class Student(Document):
    name = StringField(max_length=32, required=True)
    age = IntField(required=True)
    sex = StringField(choices=SEX_CHOICE, required=True)
    grade = StringField()
    address = StringField()
    grades = ListField(EmbeddedDocumentField(Grade))

    # 配置元数据，设置 设置集合的名字。
    meta = {
        'collection': 'student',
        'ordering': ['-age']
    }


class TestMongoEngine(object):
    def add_one(self):
        yuwen = Grade(
            name='语文',
            score=90
        )
        shuxue = Grade(
            name='数学',
            score=87
        )
        stu_obj = Student(
            name='王豫',
            age=22,
            sex='male',
            grades=[yuwen, shuxue]
        )
        # 这里为student 添加了一个额外不存在的属性，并不会保存到数据库中
        # stu_obj.remark = 'remark'
        # 可以直接修改具有的属性
        # stu_obj.name = 'remark'
        stu_obj.save()
        return stu_obj

    def get_one(self):
        return Student.objects.first()

    def get_more(self):
        return Student.objects.all()

    def get_byid(self, id):
        return Student.objects.filter(pk=id).first()

    def update_one(self):
        #       更新一条数据
        return Student.objects.filter(name='王豫').update_one(inc__age=10)

    def update(self):
        #       更新多条数据
        return Student.objects.filter(name='王豫').update(inc__age=10)

    def delete_one(self):
        return Student.objects.filter(name='王豫').first().delete()

    def delete(self):
        return Student.objects.filter(name='王豫').delete()


def run():
    obj = TestMongoEngine()
    rest = obj.add_one()
    # print(rest.id)
    # rest = obj.get_one()
    # print(rest.id)
    # print(obj.get_byid(rest.id))
    # print(rest.pk)
    # obj.update_one()
    # obj.update()
    # print(obj.delete())
    # print(obj.delete_one())


if __name__ == '__main__':
    run()
