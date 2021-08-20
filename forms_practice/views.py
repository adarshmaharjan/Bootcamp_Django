from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import MyForm, FormsModelForm
# Create your views here.


def forms_home(request):
    if request.method == 'GET':
        return render(request, 'forms_practice/forms.html', {})
    else:
        # print(request.POST.get('name'))
        return(HttpResponse(request.POST.get('name')))


def django_form(request):
    if request.method == 'GET':
        form = MyForm()
        return render(request, 'forms_practice/django_form.html', {'form': form})
    else:
        form = MyForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse('OK')
        else:
            return render(request, 'forms_practice/django_form.html', {'form': form})


def django_model_form(request):
    if request.method == 'GET':
        form = FormsModelForm()
        return render(request, 'forms_practice/forms_model.html', {'form': form})
    else:
        form = FormsModelForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return HttpResponse('OK')
        else:
            return render(request, 'forms_practice/forms_model.html', {'form': form})
