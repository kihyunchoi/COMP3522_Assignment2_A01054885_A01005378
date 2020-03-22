from enum import Enum

import pandas as pd

from Factory import *
from order import Order
import numpy as np


class SpiderType(Enum):
    Tarantula = "Tarantula"
    WolfSpider = "Wolf Spider"


class RobotBunny(Enum):
    Orange = "Orange"
    Blue = "Blue"
    Pink = "Pink"


class ToffeeVariety(Enum):
    Seasalt = "Sea Salt"
    Regular = "Regular"


class CandyCaneColour(Enum):
    Red = "Red"
    Green = "Green"


class Stuffing(Enum):
    Polyester = "Polyester Fiberfill"
    Wool = "Wool"


class Size(Enum):
    Small = "Small"
    Medium = "Medium"
    Large = "Large"


class Fabric(Enum):
    Linen = "Linen"
    Cotton = "Cotton"
    Acrylic = "Acrylic"


class EasterBunnyColour(Enum):
    White = "White"
    Grey = "Grey"
    Pink = "Pink"
    Blue = "Blue"


class OrderProcessor:

    @staticmethod
    def read_file(file_name):
        orders_list = []
        try:
            orders = pd.read_excel(file_name)
            orders.replace({np.nan: None})
            for i in range(0, len(orders)):
                ord = orders.iloc[i]
                order_number = ord["order_number"]
                product_id = ord["product_id"]
                item = ord["item"]
                name = ord["name"]
                quantity = ord["quantity"]
                details = ord[6:].replace({np.nan: None}).to_dict()
                factory = OrderProcessor.get_factory(ord["holiday"])
                order = Order(order_number, product_id, item, name, quantity, details, factory)
                orders_list.append(order)
        except FileNotFoundError as e:
            print(e)
        finally:
            return orders_list

    @staticmethod
    def validate_toy_order(order):
        """
        Validate a toy order and return an error if order contains an attribute not related to a toy.
        :param order: Order
        :return: String
        """
        error = ""
        details = order.product_details
        if order.item == "Toy":
            if details["min_age"] is None:
                error += "Minimum age not entered\n"

            if order.factory == ChristmasFactory:
                for p in details.keys():
                    if p not in ["description", "has_batteries", "min_age", "dimensions", "num_rooms"]:
                        if details[p] is not None:
                            error += "Item does not have attribute {}\n".format(p)
                    else:
                        if details[p] is None:
                            error += "Attribute {} is blank".format(p)
                if details["has_batteries"] != "N":
                    error += "This item does not contain batteries (order indicates otherwise)\n"
            elif order.factory == HalloweenFactory:
                for p in details.keys():
                    if p not in ["description", "has_batteries", "min_age", "speed", "jump_height",
                                 "has_glow", "spider_type"]:
                        if details[p] is not None:
                            error += "Item does not have attribute {}\n".format(p)
                    else:
                        if details[p] is None:
                            error += "Attribute {} is blank".format(p)
                if details["has_batteries"] != "Y":
                    error += "This item contains batteries (order indicates otherwise)\n"
                if details["has_glow"] not in ["Y", "N"]:
                    error += "Must choose Y or N for Glow in the Dark attribute\n"
                spider_types = [item.value for item in SpiderType]
                if details["spider_type"] not in spider_types:
                    error += "Spider type must be Tarantula or Wolf Spider.\n"
            elif order.factory == EasterFactory:
                for p in details.keys():
                    if p not in ["description", "has_batteries", "min_age", "num_sound", "colour"]:
                        if details[p] is not None:
                            error += "Item does not have attribute {}\n".format(p)
                    else:
                        if details[p] is None:
                            error += "Attribute {} is blank\n".format(p)
                if details["has_batteries"] != "Y":
                    error += "This item contains batteries (order indicates otherwise)\n"

                colours = [item.value for item in RobotBunny]
                if details["colour"] not in colours:
                    error += "Colour must be Orange, Blue or Pink\n"
        return error

    @staticmethod
    def validate_candy_order(order):
        """
        Validate a candy order and return an error if order contains an attribute not related to a candy.
        :param order: Order
        :return: String
        """
        error = ""
        details = order.product_details
        if order.item == "Candy":
            if order.factory == ChristmasFactory:
                for p in details.keys():
                    if p not in ["description", "has_nuts", "has_lactose", "colour"]:
                        if details[p] is not None:
                            error += "Item does not have attribute {}\n".format(p)
                    else:
                        if details[p] is None:
                            error += "Attribute {} is blank".format(p)
                if details["has_nuts"] != "N":
                    error += "This item does not contain nuts (order indicates otherwise)\n"
                if details["has_lactose"] != "N":
                    error += "This item does not contain lactose (order indicates otherwise)\n"
                colours = [item.value for item in CandyCaneColour]
                if details["colour"] not in colours:
                    error += "Colour must be Red or Green"

            elif order.factory == HalloweenFactory:
                for p in details.keys():
                    if p not in ["description", "has_nuts", "has_lactose", "variety"]:
                        if details[p] is not None:
                            error += "Item does not have attribute {}\n".format(p)
                    else:
                        if details[p] is None:
                            error += "Attribute {} is blank".format(p)
                if details["has_nuts"] != "Y":
                    error += "This item contains nuts (order indicates otherwise)\n"
                if details["has_lactose"] != "Y":
                    error += "This item contains lactose (order indicates otherwise)\n"
                variety = [item.value for item in ToffeeVariety]
                if details["variety"] not in variety:
                    error += "Toffee variety must be Sea Salt or Regular.\n"
            elif order.factory == EasterFactory:
                for p in details.keys():
                    if p not in ["description", "has_nuts", "has_lactose", "pack_size"]:
                        if details[p] is not None:
                            error += "Item does not have attribute {}\n".format(p)
                    else:
                        if details[p] is None:
                            error += "Attribute {} is blank\n".format(p)
        return error

    @staticmethod
    def validate_stuffed_order(order):
        """
        Validate a stuffed animal order and return an error if order contains an attribute not related to a stuffed
        animal.
        :param order: Order
        :return: String
        """
        error = ""
        details = order.product_details
        if order.item == "StuffedAnimal":

            if order.factory == HalloweenFactory:
                for p in details.keys():
                    if p not in ["description", "stuffing", "size", "fabric", "has_glow"]:
                        if details[p] is not None:
                            error += "Item does not have attribute {}\n".format(p)
                    else:
                        if details[p] is None:
                            error += "Attribute {} is blank".format(p)

                if details["stuffing"] != "Polyester Fibrefill":
                    error += "Stuffing can only be Polyester Fibrefill\n"
                if details["fabric"] != "Acrylic":
                    error += "Fabric must be Acrylic\n"
                if details["has_glow"] != "Y":
                    error += "Skeleton glows in the dark\n"

            elif order.factory == ChristmasFactory:
                for p in details.keys():
                    if p not in ["description", "stuffing", "size", "fabric", "has_glow"]:
                        if details[p] is not None:
                            error += "Item does not have attribute {}\n".format(p)
                    else:
                        if details[p] is None:
                            error += "Attribute {} is blank".format(p)
                if details["stuffing"] != "Wool":
                    error += "Stuffing can only be wool\n"
                if details["fabric"] != "Cotton":
                    error += "Fabric must be cotton\n"
                if details["has_glow"] != "Y":
                    error += "The reindeer nose glows in the dark\n"

            elif order.factory == EasterFactory:
                for p in details.keys():
                    if p not in ["description", "stuffing", "size", "fabric", "colour"]:
                        if details[p] is not None:
                            error += "Item does not have attribute {}\n".format(p)
                    else:
                        if details[p] is None:
                            error += "Attribute {} is blank".format(p)
                if details["stuffing"] != "Polyester Fibrefill":
                    error += "Stuffing can only be Polyester Fibrefill\n"
                if details["fabric"] != "Linen":
                    error += "Fabric must be Linen\n"
                colours = [item.value for item in EasterBunnyColour]
                if details["colour"] not in colours:
                    error += "Easter Bunny can only be White, Grey, Pink, or Blue\n"
        return error

    @staticmethod
    def get_factory(holiday):
        """
        Return the relevant Factory
        :param holiday:
        :return: Factory
        """
        if holiday == "Christmas":
            return ChristmasFactory
        elif holiday == "Halloween":
            return HalloweenFactory
        elif holiday == "Easter":
            return EasterFactory
        else:
            return None
