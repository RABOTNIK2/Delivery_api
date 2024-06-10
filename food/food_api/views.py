from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *
from .permissions import *

class KitchenViewSet(viewsets.ModelViewSet):
    queryset = Kitchen.objects.all()
    serializer_class = KitchenSerializer
    # permission_classes = [permissions.IsAdminUser]
    
class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    @action(detail=False, methods=['get'])
    def search_dish(self, request):
        query = request.query_params.get('q')
        if query is None:
            return(Response({'message': 'Введите название блюда'}, status=status.HTTP_404_NOT_FOUND))
        dish = Dish.objects.filter(dish_name__icontains = query)
        serializer = DishSerializer(dish, many=True)
        return Response(serializer.data)
    
class UserViewSet(viewsets.ViewSet):
    # permission_classes=[UserPermissions]
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=False, methods=['put'])
    def del_dish(self, request):
        try:
            query = request.data['id']
            dish_query = request.data['q']
            user = User.objects.get(pk=query)
            user_cart = User.objects.get(pk=query).cart.all()
            user_list = list(user_cart)
            if len(user_list)!=0:
                for i in user_list:
                    index= 0
                    if dish_query==i.dish_name:
                        index = user_list.index(i)
                        break
                user_list.pop(index)  
                user.cart.set(user_list)
                serializer = UserSerializer(user)  
                return Response(serializer.data)
            return(Response({'message':'Корзина путса'}, status=status.HTTP_400_BAD_REQUEST))
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=False, methods=['put'])
    def add_to_dish(self, request):
        try:
            query = request.data['id']
            dish_query = request.data['q']
            user = User.objects.get(pk=query)
            user_cart = User.objects.get(pk=query).cart.all()
            dish = Dish.objects.get(pk=dish_query)
            user_list = list(user_cart)
            user_list.append(dish)
            user.cart.set(user_list)
            serializer = UserSerializer(user)
            return Response(serializer.data) 
        except User.DoesNotExist:
            return Response({'message': 'Пользователя нет'}, status=status.HTTP_404_NOT_FOUND)
        
class OrderViewSet(viewsets.ViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        try:
            user =  User.objects.get(pk = request.data['owner'])
            user_cart = User.objects.get(pk=request.data['owner']).cart.all()
            user_list = list(user_cart)
            summ = 0
            for i in user_list:
                summ += i.price
            order = Order.objects.create(
                owner = user,
                products = user,
                make_at = request.data['make_at'],
                delivery_date = request.data['delivery_date'],
                status = request.data['status'],
                total_price = summ
            )
            order.save()
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'message': 'Ошибка'}, status=status.HTTP_400_BAD_REQUEST)
        
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        try:
            order = Order.objects.get(pk=pk)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            order = Order.objects.get(pk=pk)
            serializer = OrderSerializer(order, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            order = Order.objects.get(pk=pk)
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    #     {
    #     "id": 1,
    #     "make_at": "2024-06-06",
    #     "delivery_date": "2024-06-02",
    #     "status": "1",
    #     "total_price": 5,
    #     "owner": 1,
    #     "products": 1
    # }

    
    
# Create your views here.
