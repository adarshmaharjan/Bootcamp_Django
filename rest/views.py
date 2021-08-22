from django.http import JsonResponse
# exempt the csrf
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
# parese the JSON
from rest_framework.parsers import JSONParser
# used in validate data
from .serializers import AddTwoNumberSerializer
# Create your views here.

# rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
# serializers
from .models import Info
from .serializers import InfoSerializer


@csrf_exempt
def add_two_numbers(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Welcome to add two numbers'})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print('request-post-->', request.POST)
        print('data-->', data)

        serializer = AddTwoNumberSerializer(data=data)

        if serializer.is_valid():
            num1 = serializer.validated_data['num1']
            num2 = serializer.validated_data['num2']
            # now add these two numbers

            result = num1 + num2
            return JsonResponse({'result': result})
        print(serializer.errors)
        return JsonResponse({'error': 'Somthing went wrong'}, status=400)


@api_view(['GET', 'POST'])
def add_two_numbers_in_rest(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Welcome to add two numbers'})

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        # print('request-post-->', request.POST)
        # print('data-->', data)

        # serializer = AddTwoNumberSerializer(data=data)
        # we use this because of django rest framework
        serializer = AddTwoNumberSerializer(data=request.data)

        # if serializer.is_valid(raise_exception=True):
        #     num1 = serializer.validated_data['num1']
        #     num2 = serializer.validated_data['num2']
        #     # now add these two numbers

        #     result = num1 + num2
        #     return Response({'result': result})
        # print()
        # return Response(serializer.errors, status=400)

        serializer.is_valid(raise_exception=True)
        num1 = serializer.validated_data['num1']
        num2 = serializer.validated_data['num2']
        # now add these two numbers

        result = num1 + num2
        return Response({'result': result})


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def info_view(request, pk=None):
    if request.method == 'GET':
        qs = Info.objects.all()
        # result = []
        # for i in qs:
        #     serializer = InfoSerializer(instance=i)
        #     result.append(serializer.data)
        serializer = InfoSerializer(instance=qs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = InfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # name = serializer.validated_data['name']
        # address = serializer.validated_data['address']

        # obj = Info.objects.create(
        #     name=name,
        #     address=address
        # )
        serializer.save()
        return Response({
            'method': 'POST',
            'status': 'ok',
            'data': serializer.data
        })
    elif request.method == 'PUT':
        try:
            obj = Info.objects.get(pk=pk)
        except:
            return Response({'error': 'Doesn\'t exists'})

        serializer = InfoSerializer(data=request.data, instance=obj)
        serializer.is_valid(raise_exception=True)
        # name = serializer.validated_data['name']
        # address = serializer.validated_data['address']

        # obj.name = name
        # obj.address = address
        # obj.save()
        serializer.save()

        return Response({
            'method': 'PUT',
            'status': 'ok',
            'data': serializer.data
        })
    elif request.method == 'DELETE':
        try:
            obj = Info.objects.get(pk=pk)
        except:
            return Response({'error': 'Doesn\'t exists'})

        obj.delete()
        return Response({
            'method': 'delete',
            'status': 'ok',
            'data': None
        })
