from ShopItem import ShopItem


class Toy(ShopItem):
    """
    Abstract class for Toys
    """

    def __init__(self, has_batteries, min_age, name, description, product_id):
        """
        Construct a toy.
        :param has_batteries: Boolean
        :param min_age: Integer
        :param name: String
        :param description: String
        :param product_id: String
        """
        super().__init__(name, description, product_id)
        self.has_batteries = has_batteries
        self.min_age = min_age


class SantasWorkshop(Toy):
    """
    Create a SantasWorkshop toy.
    """

    def __init__(self, **kwargs):
        super().__init__(kwargs["has_batteries"], kwargs["min_age"], kwargs["name"],
                         kwargs["description"], kwargs["product_id"])
        self.dimensions = kwargs["dimensions"]
        self.num_rooms = kwargs["num_rooms"]


class RCSpider(Toy):
    """
    Create an RC Spider toy.
    """

    def __init__(self, **kwargs):
        super().__init__(kwargs["has_batteries"], kwargs["min_age"], kwargs["name"],
                         kwargs["description"], kwargs["product_id"])
        self.speed = kwargs["speed"]
        self.jump_height = kwargs["jump_height"]
        self.has_glow = kwargs["has_glow"]
        self.spider_type = kwargs["spider_type"]


class RobotBunny(Toy):
    """
    Create a Robot Bunny toy.
    """

    def __init__(self, **kwargs):
        super().__init__(kwargs["has_batteries"], kwargs["min_age"], kwargs["name"],
                         kwargs["description"], kwargs["product_id"])
        self.num_sound = kwargs["num_sound"]
        self.colour = kwargs["colour"]
