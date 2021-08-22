
from rest_framework import serializers
from .models import Info


class AddTwoNumberSerializer(serializers.Serializer):
    num1 = serializers.IntegerField()
    num2 = serializers.IntegerField()


class InfoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=100)

    def create(self, validated_data):
        print('Context on serializer', self.context)
        return Info.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.address = validated_data['address']
        instance.save()
        return instance


class InfoModelSerializer(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Info
        #!not working
        # fields = ['name', 'address', 'messages']
        fields = ['name', 'address']

    #!not working
    # @staticmethod
    #!not working
    # def get_message(self, obj):
    #     name = obj.name
    #     return f'Hi My name is {name}'
    #!not working
    # @staticmethod

    def validate_name(self, name):
        if len(name) <= 1:
            raise serializers.ValidationError(
                'Length of name shouldn\'t be greater than 1')
        return name

    def validate(self, data):
        name = data['name']
        address = data['address']
        if name == address:
            raise serializers.ValidationError(
                'Name and Address cannot be same')
        print(data)
        return data
