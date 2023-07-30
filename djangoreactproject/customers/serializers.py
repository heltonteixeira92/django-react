from rest_framework import serializers
from .models import Customers

'''
Um serializador no Django REST Framework 
permite que as instâncias de modelos complexas
 e o QuerySets sejam convertidos em formato JSON 
 para consumo de API. A classe de serializadores 
 também pode funcionar na outra direção, 
 fornecendo mecanismos para processar e 
 desserializar dados em modelos Django e QuerySets.
'''


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        # campos que serão serializados
        fields = ('pk', 'first_name', 'last_name', 'email', 'phone', 'address', 'description')
