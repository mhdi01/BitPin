from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        request.data['username'] = request.data['username'].lower()
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

        
