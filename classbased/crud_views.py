from io import SEEK_SET
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from .models import UserInfo

from .forms import UserInfoModelForm

from django.urls import reverse_lazy


class Create(CreateView):
    form_class = UserInfoModelForm
    template_name = 'classbased/create.html'
    # success_url = 'classbased/list/'
    success_url = reverse_lazy('classbased:list')

    # def get_success_url(self):
    #     return reverse('classbased:list')


class List(ListView):
    template_name = 'classbased/list.html'
    # queryset = UserInfo.objects.all()
    model = UserInfo
    context_object_name = 'data'

    # def get_context_data(self, **kwargs):
    #     pass

    # def get_queryset(self):
    #     return UserInfo.objects.all()


class Detail(DetailView):
    model = UserInfo
    template_name = 'classbased/detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'data'


class Update(UpdateView):
    form_class = UserInfoModelForm
    pk_url_kwarg = 'id'
    success_url = '/classbased/list'
    model = UserInfo
    template_name = './classbased/update.html'

    def form_valid(self, form):
        print('Form is valid')
        return super().form_valid(form)


class Delete(DeleteView):
    # pk_url_kwarg = 'id'
    model = UserInfo
    success_url = '/classbased/list/'
    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)
