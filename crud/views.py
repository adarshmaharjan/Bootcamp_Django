from django.shortcuts import get_object_or_404, redirect, render
from .models import UserInfo

# Form
from .forms import UserInfoModelForm
# Create your views here.


def list_all_user(request):
    all_users = UserInfo.objects.all()
    # print(all_users)
    context = {
        'data': all_users
    }
    return render(request, './crud/list.html', context=context)


def detail_view(request, user_id):
    # try:
    #     data = UserInfo.objects.get(id=user_id)
    # except:
    #     raise Exception("User doesn\'t Exists")
    data = get_object_or_404(UserInfo, id=user_id)
    context = {
        'data': data
    }
    return render(request, 'crud/detail.html', context=context)


def create_user_info(request):

    if request.method == 'POST':

        form = UserInfoModelForm(request.POST)
        if form.is_valid():
            print(form.changed_data)
            print("form is valid")
            form.save()
            return redirect('/crud/list')
        else:
            print("Invalid Form")
    else:
        form = UserInfoModelForm()
    context = {
        'form': form
    }
    return render(request, './crud/create.html', context=context)


def update_user_info(request, user_id):
    user_object = get_object_or_404(UserInfo, id=user_id)
    if request.method == 'POST':

        form = UserInfoModelForm(request.POST, instance=user_object)
        if form.is_valid():
            print(form.changed_data)
            print("form is valid")
            form.save()
            return redirect(f'/crud/detail/{user_id}')
        else:
            print("Invalid Form")
    else:
        form = UserInfoModelForm(instance=user_object)
    context = {
        'form': form
    }
    return render(request, './crud/update.html', context=context)


def delete_user_info(request, user_id):
    if request.method == 'GET':
        user_object = get_object_or_404(UserInfo, id=user_id)
        user_object.delete()
    return redirect('/crud/list')
