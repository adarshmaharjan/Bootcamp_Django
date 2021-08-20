from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.


def render_static(request):
    return render(request, 'static.html', {})


def manage_media(request):
    if request.method == 'POST':
        print("Post data", request.POST)
        print('files', request.FILES)
        file_obj = request.FILES['test-file']
        print('File-Name', file_obj.name)
        fs = FileSystemStorage()
        # _file_name = 'image/my/show.jpg'
        # filename = fs.save(_file_name, file_obj)

        filename = fs.save(file_obj.name, file_obj)

        # file_url = fs.url(filename)
        # print('file_name', filename)
        # print('file_url', file_url)

    return render(request, 'media.html', {})
