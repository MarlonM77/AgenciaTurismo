from django.conf                        import settings
from rest_framework                     import generics, status
from rest_framework.response            import Response
from rest_framework.permissions         import IsAuthenticated
from rest_framework_simplejwt.backends  import TokenBackend

from authApp.models.plan                import Plan
from authApp.serializers.planSerializer import PlanSerializer

class PlanUserView(generics.RetrieveAPIView):
    serializer_class   =  PlanSerializer
    permission_classes =  (IsAuthenticated, )
    queryset           =  Plan.objects.all()

    def get(self, request, *args, **kwargs):                  

        return super().get(request, *args, **kwargs)

    
class PlanCreateView(generics.CreateAPIView):
    serializer_class    =  PlanSerializer
    permission_classes  =  (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        print("Request:", request)
        print("Args:", args)
        print("KWArgs:", kwargs)
        token           = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend    = TokenBackend(algorithm = settings.SIMPLE_JWT['ALGORITHM'])
        valid_data      = tokenBackend.decode(token, verify = False)

        if valid_data['user_id'] != request.data['user_id']:
            stringResponse = {'detail' : 'Unauthorized Request'}
            return Response(stringResponse, status = status.HTTP_401_UNAUTHORIZED)

        serializer = PlanSerializer(data = request.data['plan_data'])
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response("Plan Reservado", status = status.HTTP_201_CREATED)

    
class PlanUpdateView(generics.UpdateAPIView):
    serializer_class    =   PlanSerializer
    permission_classes  =   (IsAuthenticated, )
    queryset             =   Plan.objects.all()

    def put(self, request, *args, **kwargs):
        print("Request:", request)
        print("Args:", args)
        print("KWArgs:", kwargs)
        token           = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend    = TokenBackend(algorithm = settings.SIMPLE_JWT['ALGORITHM'])
        valid_data      = tokenBackend.decode(token, verify = False)

        if valid_data['user_id'] != request.data['user_id']:
            stringResponse = {'detail' : 'Unauthorized Request'}
            return Response(stringResponse, status = status.HTTP_404_UNAUTHORIZED)
        
        return super().update(request, *args, **kwargs)


class PlanDeleteView(generics.DestroyAPIView):
    serializer_class    =   PlanSerializer
    permission_classes  =   (IsAuthenticated, )
    queryset            =   Plan.objects.all()

    def delete(self, request, *args, **kwargs):
        print("Request:", request)
        print("Args:", args)
        print("Kwargs:", kwargs)
        token           = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend    = TokenBackend(algorithm = settings.SIMPLE_JWT['ALGORITHM'])
        valid_data      = tokenBackend.decode(token, verify = False)

        if valid_data['user_id'] != request.data['user_id']:
            stringResponse  = {'detail' : 'Unauthorized Request'}
            return Response(stringResponse, status = status.HTTP_401_UNAUTHORIZED)

        return super().destroy(request, *args, **kwargs)


    
