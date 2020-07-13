# -*- coding: utf-8 -*-

from django.http import HttpResponse

from backend.models import User

# 数据库操作
def testdb(request):
    test1 = User(name='runoob')
    test1.save()

    test2 = User(name='测试')
    test2.save()

    test3 = User(name='成功')
    test3.save()
    return HttpResponse("<p>数据添加成功！</p>")


def showdb(request):
    # 初始化
    response = ""
    response1 = ""


    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = User.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    # response2 = User.objects.filter(id=1)

    # 获取单个对象
    # response3 = User.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    # User.objects.order_by('name')[0:2]

    #数据排序
    # User.objects.order_by("id")

    # 上面的方法可以连锁使用
    # User.objects.filter(name="runoob").order_by("id")

    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")


def updatedb(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = User.objects.get(id=1)
    test1.name = 'Google'
    test1.save()

    # 另外一种方式
    #Test.objects.filter(id=1).update(name='Google')

    # 修改所有的列
    # Test.objects.all().update(name='Google')

    return HttpResponse("<p>修改成功</p>")

def destroydb(request):
    # 删除id=1的数据
    test1 = User.objects.get(id=1)
    test1.delete()

    # 另外一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    # Test.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")