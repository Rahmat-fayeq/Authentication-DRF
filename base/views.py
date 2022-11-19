from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, views
import random
import string
from django.core.mail import send_mail
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from .models import User,Rest_password
from .serializers import UserSerializer

# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def showRoutes(request):
    routes = [
        '/api/register/',
        'api/password-forgot/',
        'api/password-reset/',
        '/api/token/',
        '/api/token/refresh/',
        '/api/news/',
        '/api/user/reset-password'
    ]
    return Response(routes)

class RegisterViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer    


class ForgotPasswordAPIView(views.APIView):
    def post(self, request):
        token = ''.join(random.choice(string.ascii_lowercase+ string.ascii_uppercase + string.digits) for _ in range(10))
    
        Rest_password.objects.create(
            email = request.data['email'],
            token = token
        )

        url = 'http://localhost:3000/reset-password/'+token    
        send_mail(
            subject = 'Reset Your Password',
            message = 'Click <a href="%s">here</a> to reset your password !' %url,
            from_email = 'example@example.com',
            recipient_list = [request.data['email']]     
        )

        
        return Response({
            'message': 'Link has been sent to your email, please confirm it.',
            'url': 'Click <a href="%s">here</a> to reset your password' %url
        })
    

@api_view(['POST'])
def ResetPasswordView(request):
    data = request.data 

    if(data['password'] != data['password_confirm']):
        return Response('Passwords do not match !', status.HTTP_400_BAD_REQUEST)

    reset_password = Rest_password.objects.filter(token=data['token']).first()

    if not reset_password:
     return Response('Invalid link !', status.HTTP_400_BAD_REQUEST)

    user = User.objects.filter(email=reset_password.email).first()

    if not user:
        return Response('User not found !', status.HTTP_404_NOT_FOUND) 

    user.set_password(data['password'])
    user.save()

    return Response({'Password reset successfully !'}, status.HTTP_200_OK)    

@api_view(['put'])
def PasswordResetView(request, id):
    user = User.objects.filter(pk=id).first()
    if not user:
        return Response('User not found', status.HTTP_404_NOT_FOUND)

    if request.data['password'] != request.data['password_confirm']:
        return Response('Password and Confirm password do not match !', status.HTTP_400_BAD_REQUEST)
    
    user.set_password(request.data['password'])
    user.save()

    return Response('Password changed successfully', status.HTTP_200_OK)