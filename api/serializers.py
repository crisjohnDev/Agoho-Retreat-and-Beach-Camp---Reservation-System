from rest_framework import serializers
from accounts.models import User
from customer.models import Customer
from core.models import Rooms, Reservation



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )

        return user
    
class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"
        read_only_fields = ["user"]


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rooms
        fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = "__all__"
        read_only_fields = (
            "customer",
            "status",
            "total_price",
            "created_at",
        )