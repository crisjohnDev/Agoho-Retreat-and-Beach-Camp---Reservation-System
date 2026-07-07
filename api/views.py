
from decimal import Decimal
from datetime import date
# React
from rest_framework import generics
from .serializers import RegisterSerializer, CustomerSerializer, RoomSerializer, ReservationSerializer
from rest_framework.generics import ListAPIView

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from core.models import Rooms

# Mobile
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class CustomerProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(
                user=request.user
            )

            return Response(serializer.data)

        return Response(serializer.errors, status=400)
    
class RoomListView(ListAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer

class ReservationCreateView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        customer = request.user.customer_profile

        room_id = request.data.get("room")
        check_in = request.data.get("check_in")
        check_out = request.data.get("check_out")

        room = Rooms.objects.get(id=room_id)

        serializer = ReservationSerializer(data=request.data)

        if serializer.is_valid():

            checkin = date.fromisoformat(check_in)
            checkout = date.fromisoformat(check_out)

            nights = (checkout - checkin).days

            total_price = Decimal(room.price) * nights

            serializer.save(
                customer=customer,
                room=room,
                total_price=total_price
            )

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)