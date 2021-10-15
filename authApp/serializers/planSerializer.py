from authApp.models.plan    import Plan
from rest_framework         import serializers

from authApp.models.user import User

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['valor','fecha_inicio','fecha_fin', 'nombre_plan', 'descripcion', 'cant_personas']
    















        