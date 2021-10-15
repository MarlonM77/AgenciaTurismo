from rest_framework             import serializers
from authApp.models.user        import User
from authApp.models.plan        import Plan
from .planSerializer            import PlanSerializer    


class UserSerializer(serializers.ModelSerializer):

    plan = PlanSerializer
    class Meta:
        model  = User
        fields = ['id', 'username', 'password', 'name', 'email', 'plan']

    def create(self, validated_data):
        planData     = validated_data.pop('plan')
        userInstance = User.objects.create(**validated_data)
        Plan.objects.create(user = userInstance, **planData)
        return userInstance        

    def to_representation(self, obj):
        user    = User.objects.get(id   = obj.id)
        plan    = Plan.objects.get(user = obj.id)

        return {
        'id':       user.id,
        'username': user.username,
        'name':     user.name,
        'email':    user.email,
        'plan': {
            'id_plan':         plan.id,
            'valor':           plan.valor,    
            'fecha_inicio':    plan.fecha_inicio,
            'fecha_fin':       plan.fecha_fin,
            'nombre_plan':     plan.nombre_plan,
            'cant_personas':   plan.cant_personas
            }
        }
