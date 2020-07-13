from django.shortcuts import render, HttpResponse
from forground.my_form import EmpForm
from forground import models
from django.core.exceptions import ValidationError
# Create your views here.

def add_emp(request):
    if request.method == "GET":
        form = EmpForm()
        return render(request, "add_emp.html", {"form": form})
    else:
        form = EmpForm(request.POST)
        if form.is_valid():  # 进行数据校验
            # 校验成功
            data = form.cleaned_data  # 校验成功的值，会放在cleaned_data里。
            data.pop('r_email')

            models.Publish.objects.create(**data)
            return redirect("/index/")
        else:
            clean_errors = form.errors.get("__all__")
            return render(request, "add_emp.html", {"form": form, "clean_errors": clean_errors})