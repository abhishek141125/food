from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FoodItem
from .serializers import FoodItemSerializer

@api_view(["GET"])
def get_foods(request):
    foods = FoodItem.objects.all()
    return Response(FoodItemSerializer(foods, many=True).data)