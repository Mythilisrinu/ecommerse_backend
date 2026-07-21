import traceback
import django
from rest_framework.test import APIRequestFactory
from ecomapp.views import registerUser
from django.contrib.auth.models import User

django.setup()
User.objects.filter(email='register@example.com').delete()
factory = APIRequestFactory()
request = factory.post('/api/users/register/', {'fname':'Test','lname':'User','email':'register@example.com','password':'register123'}, format='json')
try:
    response = registerUser(request)
    print('status', response.status_code)
    print(response.data)
except Exception:
    traceback.print_exc()
