from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import ProductSerializer, MyTokenObtainPairSerializer, UserSerializer, UserSerializerWithToken
from .models import Products
from django.contrib.auth.models import User

from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .utils import TokenGenerator, generate_token
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render
from django.views.generic import View

@api_view(['GET'])
def getRoutes(request):
    return Response('API is working')


@api_view(['GET'])
def getProducts(request):
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = Products.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        first_name = data.get('fname') or data.get('first_name') or data.get('firstName') or ''
        last_name = data.get('lname') or data.get('last_name') or data.get('lastName') or ''
        email = data.get('email')
        password = data.get('password')
        username = data.get('username') or email

        if not email or not password:
            return Response({'details': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
            is_active=True,
        )

        try:
            email_subject = 'Activate your account'
            message = render_to_string('activate.html', {
                'user': user,
                'domain': '127.0.0.1:8000',
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user),
            })
            email_message = EmailMessage(
                email_subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
            )
            email_message.send()
        except Exception:
            pass

        return Response({'details':'Activate your account, please check the gmail for account activation'})
    except Exception as e:
        message = {'details': str(e)}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception:
            user = None

        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            return render(request, "activatesuccess.html")

        return render(request, "activatefail.html")