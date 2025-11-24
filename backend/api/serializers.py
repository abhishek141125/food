from restframework import serializers
from .moduls import FoodItem

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = "_all_"