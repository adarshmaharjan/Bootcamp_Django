# from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import View
from django.views.generic import TemplateView, RedirectView

# Create your views here.


class FirstView(View):
    # get
    # post method --> post()

    def get(self, request, *args, **kwargs):
        return HttpResponse("This is Get")

    def post(self, request, *args, **kwargs):
        return HttpResponse("This is POST")


class FirstTemplate(TemplateView):
    template_name = 'classbased/test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg'] = "Hello World"
        return context


class FirstTemplateRedirect(RedirectView):
    url = '/classbased/first-test/'
