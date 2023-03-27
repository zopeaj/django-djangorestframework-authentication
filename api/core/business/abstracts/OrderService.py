from order.models import Order
from order.repository import OrderRepository

class OrderService:
    def __init__(self, orderRepository):
        self.orderRepository = orderRepository

    def saveOrder(self):
        pass

    def deleteOrder(self, order_id):
        pass

    def updateOrder(self, order, order_id):
        pass

orderService = OrderService(OrderRepository(Order()))
