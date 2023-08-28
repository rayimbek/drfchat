import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import *

class ClubSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default= serializers.CurrentUserDefault())
    class Meta:
        model = Club
        fields = "__all__"


"""
class ClubSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    mission = serializers.CharField()
    cat_id = serializers.IntegerField()
    data_created = serializers. DateTimeField(read_only=True)

    def create(self, validated_data):
        return Club.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.mission = validated_data.get("mission", instance.mission)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance

    def delete(self,instance):

        instance.delete()

"""
"""
def encode():
    model = ClubModel('Basketball club', ' dwadasdasd', 'sssfthtfhoko ccadw')
    model_sr = ClubSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)

def decode():
    stream = io.BytesIO(b'{"name":"Basketball club","description":" dwadasdasd","mission":"sssfthtfhoko ccadw"}')
    data = JSONParser().parse(stream)
    serializer = ClubSerializer(data = data)
    serializer.is_valid()
    print(serializer.validated_data)
"""