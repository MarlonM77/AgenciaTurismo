from authApp.models.plan    import Plan
from rest_framework         import serializers

from authApp.models.user import User

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['valor','fecha_inicio','fecha_fin', 'nombre_plan', 'descripcion', 'cant_personas']
    
    def to_representation(self, obj):
        user = User.objects.get(id = obj.user)
        plan = Plan.objects.get(id = obj.id)

        return{
            'valor':           plan.valor,
            'fecha_inicio':    plan.fecha_inicio,
            'fecha_fin':       plan.fecha_fin,
            'nombre_plan':     plan.nombre_plan,
            'descripcion':     plan.descripcion,
            'cant_personas':   plan.cant_personas,
            'user': {
                'username':   user.username,
                'name':       user.name,
                'email':      user.email
            }
        }















        