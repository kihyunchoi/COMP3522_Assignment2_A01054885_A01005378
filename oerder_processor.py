import pandas as pd

from Factory import *
from order import Order


class OrderProcessor:

    @staticmethod
    def read_file(file_name):
        orders = []
        try:
            received_orders = pd.read_excel(file_name).to_dict('records')
            # print(received_orders)

            for i in received_orders:
                order_number = i.get("order_number")
                holiday = i.get("holiday")
                item = i.get("item")
                name = i.get("name")
                quantity = i.get("quantity")
                product_id = i.get("product_id")

                keys = [
                    'order_number',
                    'holiday',
                    'item',
                    'name',
                    'quantity',
                    'product_id',
                    'description',
                    'has_batteries',
                    'min_age',
                    'dimensions',
                    'num_rooms',
                    'speed',
                    'jump_height',
                    'has_glow',
                    'spider_type',
                    'num_sound',
                    'colour',
                    'has_lactose',
                    'has_nuts',
                    'variety',
                    'pack_size',
                    'stuffing',
                    'size',
                    'fabric'
                ]

                order_quantity = {product_id: quantity}

                # product_details = {product_id: {x: i[x] for x in keys}}
                # print(product_details)

                # order = Order(order_number, product_id, item, name, quantity, product_details)
                # print(order)

                # order = OrderProcessor.factory_mapping(holiday, item, product_details)
                # print(order)
                orders.append(order_quantity)

        except FileNotFoundError as e:
            print(e)

        finally:
            return orders

    # @staticmethod
    # def factory_mapping(holiday, item, product_details):
    #     if holiday == "Easter":
    #         if item == "Toy":
    #             return EasterFactory.create_toy(product_details)
    #         elif item == "Stuffed Animal":
    #             return EasterFactory.create_stuffed_animal(product_details)
    #         elif item == "Candy":
    #             return EasterFactory.create_candy(product_details)
    #     elif holiday == "Halloween":
    #         if item == "Toy":
    #             return HalloweenFactory.create_toy(product_details)
    #         elif item == "Stuffed Animal":
    #             return HalloweenFactory.create_stuffed_animal(product_details)
    #         elif item == "Candy":
    #             return HalloweenFactory.create_candy(product_details)
    #     elif holiday == "Christmas":
    #         if item == "Toy":
    #             return ChristmasFactory.create_toy(product_details)
    #         elif item == "Stuffed Animal":
    #             return ChristmasFactory.create_stuffed_animal(product_details)
    #         elif item == "Candy":
    #             return ChristmasFactory.create_candy(product_details)
