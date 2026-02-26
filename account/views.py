from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Register
from .serializers import LoginSerializer
from rest_framework import status


class RegisterView(APIView):
    def post(self,request):
        data=Register(data=request.data)

        if data.is_valid():
            data.save()   
            return Response({"User created"})
        return Response(data.errors)

class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        breakpoint()
        if serializer.is_valid():
            return Response(serializer.validated_data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    