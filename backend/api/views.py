from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import FoodItem, User
from .serializers import FoodItemSerializer, UserSerializer

@api_view(["GET"])
def get_foods(request):
    foods = FoodItem.objects.all()
    return Response(FoodItemSerializer(foods, many=True).data)

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username_or_contact = request.data.get('username_or_contact')
    password = request.data.get('password')
    try:
        user = User.objects.get(
            models.Q(username=username_or_contact) |
            models.Q(email=username_or_contact) |
            models.Q(contact=username_or_contact)
        )
        if user.password == password:
            return Response({'message': 'Login successful', 'user': UserSerializer(user).data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
