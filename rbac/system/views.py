from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from django.contrib.auth import get_user_model 
from .models import Role,Feature,UserFlow,Security

User = get_user_model() 

@api_view(['POST']) 
def create_user(request): 
    creator = request.user 
    data = request.data 
    try: 
        role = Role.objects.get(name=data['role']) 
    except Role.DoesNotExist: 
        return Response({"error": "Invalid role"}) 
    if creator.role.level >= role.level: 
        return Response({"error": "Cannot create equal/higher role user"}, status=403) 
    user = User.objects.create_user( 
        username=data['username'], 
        password=data['password'], 
        role=role, 
        email=data.get('email') 
    ) 
    return Response({"message": "User created", 
                     "user_id": user.id}) 

@api_view(['POST']) 
def create_user(request): 
    creator = request.user 
    data = request.data 
    try: 
        feature = Feature.objects.get(name=data['feature']) 
    except Feature.DoesNotExist: 
        return Response({"error": "Invalid feature"}) 
    if creator.role.level >= feature.level: 
        return Response({"error": "Cannot create equal/higher feature user"}, status=403) 
    user = User.objects.create_user( 
        username=data['username'], 
        password=data['password'], 
        role=role, 
        email=data.get('email') 
    ) 
    return Response({"message": "User created", 
                     "user_id": user.id}) 