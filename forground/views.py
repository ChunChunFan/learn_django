from django.shortcuts import render,HttpResponse
from forground import models
from forground.models import Sites
from django.db.models import Avg,Max,Min,Count,Sum  #   引入函数

def add_book(request):
    return render(request, 'book_add.html')

def save_add_book(request):
    book = Sites(title=request.POST['title'],price=request.POST['price'],publish=request.POST['publish'],pub_date=request.POST['pub_date'])
    book.save()
    # books = models.Book.objects.create(title="如来神掌",price=200,publish="功夫出版社",pub_date="2010-10-10")
    return render(request, "book_add.html", {"rlt": '添加成功'})

def save_many_data(request):
    # 保存出版社对象
    models.Publish.objects.create(name='华山出版社', city='华山', email='hs@163.com')
    models.Publish.objects.create(name='明教出版社', city='黑木崖', email='mj@163.com')
    # 保存author_detail
    models.AuthorDetail.objects.create(gender=1,tel='13432335433',addr='华山',birthday="1994-5-23")
    models.AuthorDetail.objects.create(gender=1,tel='13943454554',addr='黑木崖',birthday="1961-8-13")
    models.AuthorDetail.objects.create(gender=0,tel='13878934322',addr='黑木崖',birthday="1996-5-20")
    # 保存author
    models.Author.objects.create(name='令狐冲',age=25,au_detail_id=1)
    models.Author.objects.create(name='任我行',age=58,au_detail_id=2)
    models.Author.objects.create(name='任盈盈',age=23,au_detail_id=3)

    return HttpResponse("成功")


def show_many_data(request):
    #  获取出版社对象
    pub_obj = models.Publish.objects.filter(pk=1).first()
    #  给书籍的出版社属性publish传出版社对象
    book = models.Book.objects.create(title="菜鸟教程", price=200, pub_date="2010-10-10", publish=pub_obj)

    #  获取作者对象
    chong = models.Author.objects.filter(name="令狐冲").first()
    ying = models.Author.objects.filter(name="任盈盈").first()
    #  获取书籍对象
    book = models.Book.objects.filter(title="菜鸟教程").first()
    #  给书籍对象的 authors 属性用 add 方法传作者对象
    book.authors.add(chong, ying)


    book_obj = models.Book.objects.get(id=1)
    author_list = models.Author.objects.filter(id__gt=2)
    book_obj.authors.add(*author_list)  # 将 id 大于2的作者对象添加到这本书的作者集合中
    # 方式二：传对象 id
    book_obj.authors.add(*[1,3]) # 将 id=1 和 id=3 的作者对象添加到这本书的作者集合中


    ying = models.Author.objects.filter(name="任盈盈").first()
    book = models.Book.objects.filter(title="冲灵剑法").first()
    ying.book_set.add(book)


    # 关联创建
    pub = models.Publish.objects.filter(name="明教出版社").first()
    wo = models.Author.objects.filter(name="任我行").first()
    book = wo.book_set.create(title="吸星大法", price=300, pub_date="1999-9-19", publish=pub)


    # 从关联对象集中移除执行的模型对象
    author_obj =models.Author.objects.get(id=1)
    book_obj = models.Book.objects.get(id=1)
    author_obj.book_set.remove(book_obj)

    #清空独孤九剑关联的所有作者
    book = models.Book.objects.filter(title="菜鸟教程").first()
    book.authors.clear()

    # 一对一查询
    book = models.Book.objects.filter(pk=1).first()
    res = book.publish.city

    #一对多查询
    pub = models.Publish.objects.filter(name="明教出版社").first()
    res = pub.book_set.all()

    book = models.Book.objects.filter(title="菜鸟教程").first()
    res = book.authors.all()

    #查询菜鸟出版社出版过的所有书籍的名字与价格
    res = models.Book.objects.filter(publish__name="华山出版社").values_list("title", "price")
    res = models.Book.objects.filter(authors__name="任我行").values_list("title")
    res = models.AuthorDetail.objects.filter(author__name="任我行").values_list("tel")

    # 跨表取数据
    res = models.Publish.objects.filter(name="明教出版社").values_list("book__title","book__price")
    res = models.Author.objects.filter(name="任我行").values_list("book__title")
    res = models.Author.objects.filter(name="任我行").values_list("au_detail__tel")


    return HttpResponse(res)

def juhe_select(request):
  #res = models.Book.objects.aggregate(Avg("price"))
  res = models.Book.objects.aggregate(c=Count("id"),max=Max("price"),min=Min("price"))
  print(res,type(res))
  return HttpResponse('ok')





