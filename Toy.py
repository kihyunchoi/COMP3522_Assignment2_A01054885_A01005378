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

    def __hash__(self):
        return hash((self.name, self.product_id, self.description, self.min_age, self.has_batteries))

    def __eq__(self, other):
        if not isinstance(other, Toy):
            return NotImplemented

        return (self.name == other.name and self.product_id == other.product_id
                and self.description == other.description and self.min_age == self.min_age
                and self.has_batteries == other.has_batteries)


class SantasWorkshop(Toy):
    """
    Create a SantasWorkshop toy.
    """

    def __init__(self, name, product_id, **kwargs):
        super().__init__(kwargs["has_batteries"], kwargs["min_age"], name,
                         kwargs["description"], product_id)
        self.dimensions = kwargs["dimensions"]
        self.num_rooms = kwargs["num_rooms"]

    # def __str__(self):
    #     return f"Name : {self.name}\n" \
    #            f"Product id : {self.product_id}\n" \
    #            f"Has batteries : {self.has_batteries}\n" \
    #            f"Min age : {self.min_age}\n" \
    #            f"Dimensions : {self.dimensions}\n" \
    #            f"Number of Rooms : {self.num_rooms}\n"


class RCSpider(Toy):
    """
    Create an RC Spider toy.
    """

    def __init__(self, name, product_id, **kwargs):
        super().__init__(kwargs["has_batteries"], kwargs["min_age"], name,
                         kwargs["description"], product_id)
        self.speed = kwargs["speed"]
        self.jump_height = kwargs["jump_height"]
        self.has_glow = kwargs["has_glow"]
        self.spider_type = kwargs["spider_type"]

    # def __str__(self):
    #     return f"Name : {self.name}\n" \
    #            f"Product id : {self.product_id}\n" \
    #            f"Has batteries : {self.has_batteries}\n" \
    #            f"Min age : {self.min_age}\n" \
    #            f"Speed : {self.speed}\n" \
    #            f"Jump height : {self.jump_height}\n" \
    #            f"Has glow : {self.has_glow}\n" \
    #            f"Spider type : {self.spider_type}\n"


class RobotBunny(Toy):
    """
    Create a Robot Bunny toy.
    """

    def __init__(self, name, product_id, **kwargs):
        super().__init__(kwargs["has_batteries"], kwargs["min_age"], name,
                         kwargs["description"], product_id)
        self.num_sound = kwargs["num_sound"]
        self.colour = kwargs["colour"]

    # def __str__(self):
    #     return f"Name : {self.name}\n" \
    #            f"Product id : {self.product_id}\n" \
    #            f"Has batteries : {self.has_batteries}\n" \
    #            f"Min age : {self.min_age}\n" \
    #            f"Num sound : {self.num_sound}\n" \
    #            f"Colour : {self.colour}\n"
