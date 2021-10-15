'''
from rest_framework                        import serializers
from authApp.models.guia                   import guia



class guiaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = User_guia
        fields = ['id', 'user', 'nombre', 'cedula', 'contacto', 'tipo_turismo', 'descripcion']

    def create(self, validated_data):
        userInstance = User_guia.objects.create(**validated_data)
        return userInstance

    def to_representation(self, obj):
        user    = User_guia.objects.get(id = obj.id)
        return {                
        'user':             user.user,
        'nombre':           user.nombre,
        'cedula':           user.cedula,
        'contacto':         user.contacto,
        'tipo_turismo':     user.turismo,
        'descripcion':      user.descripcion,
        }
'''