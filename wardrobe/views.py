from django.shortcuts import render

def runoob(request):
    context          = {}
    context['hello'] = 'Hello World!'
    # return render(request, 'runoob.html', context)

    views_name = "string"
    # return  render(request,"runoob.html", {"name":views_name})

    views_list = ["数组1","数组2","数组3"]
    # return  render(request,"runoob.html", {"views_list":views_list})

    views_dict = {"name":"hash1"}
    # return render(request, "runoob.html", {"views_dict": views_dict})

    cs1 = {"name":views_name, "views_list":views_list, "views_dict": views_dict}

    name1 =0
    # return render(request, "runoob.html", {"name1": name1})

    name ="菜鸟教程"
    # return render(request, "runoob.html", {"name": name})

    import datetime
    now  =datetime.datetime.now()
    # return render(request, "runoob.html", {"time": now})

    cs2 = {"name1": name1, "name": name, "time": now}

    views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
    # return render(request, "runoob.html", {"views_str": views_str})
    cs3 = {"views_str": views_str}

    return render(request, 'runoob.html', {'cs1': cs1, 'cs2': cs1, 'cs3': cs3})