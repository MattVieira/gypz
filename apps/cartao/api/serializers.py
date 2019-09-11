import numpy as np
from rest_framework.serializers import ModelSerializer

from apps.cartao.models import CardCreate



class CardSerializers(ModelSerializer):

    class Meta:
        model = CardCreate
        fields = ('id', 'name','cpf','email', 'salary')


    def create(self,validated_data):

        x = np.random.randint(1,999,1)
        card = CardCreate.objects.create(**validated_data)
        card.points = x
        card.status = True

        if x<600:
            card.status = False
        elif x <=799:
            card.limit = validated_data['salary'] * 1.5
        elif x <= 950:
            card.limit = validated_data['salary']*3
        elif x>950:
            card.limit = np.random.randint(validated_data['salary'],1000000,1)
        try:
            card.save()
            return card
        except:
            return {'message': 'This is error'}


