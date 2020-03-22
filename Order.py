import pandas as pd

from Factory import ChristmasFactory, HalloweenFactory, EasterFactory


class Order:
    """
    An online store order.
    """

    def __init__(self, order_number, product_id, item, name, quantity, details: dict, factory):
        """

        :param order_number:
        :param product_id:
        :param item:
        :param name:
        :param details:
        """
        self.order_number = order_number
        self.product_id = product_id
        self.item = item
        self.name = name
        self.details = details
        self.factory = factory
        self.quantity = quantity

    def __str__(self):
        return self.product_id


class OrderProcessor:

    @staticmethod
    def read_orders(file_name):
        orders_list = []
        orders = pd.read_excel(file_name)
        for i in range(0, len(orders)):
            ord = orders.iloc[i]
            order_number = ord["order_number"]
            product_id = ord["product_id"]
            item = ord["item"]
            name = ord["name"]
            quantity = ord["quantity"]
            details = ord[6:].to_dict()
            factory = None
            if ord["holiday"] == "Christmas":
                factory = ChristmasFactory
            elif ord["holiday"] == "Halloween":
                factory = HalloweenFactory
            elif ord["holiday"] == "Easter":
                factory = EasterFactory
            else:
                print("Factory could not be found.")
            order = Order(order_number, product_id, item, name, quantity, details, factory)
            orders_list.append(order)
        for i in orders_list:
            print(i)


OrderProcessor.read_orders("orders.xlsx")
