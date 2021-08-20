from django.shortcuts import render
from rest_framework import request
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class DemoView(APIView):
    def get(self, *args, **kwargs):
        request = self.request
        params = request.query_params
        print(params)
        a = int(params['a'])
        b = int(params['b'])

        print(request.method)
        return Response({
            "sum": a + b
        })

    def post(self, *args, **kwargs):
        return Response({
            "message": "Post is Working"
        })
