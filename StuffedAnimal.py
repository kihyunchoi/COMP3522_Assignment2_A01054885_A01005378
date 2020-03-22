from ShopItem import ShopItem


class StuffedAnimal(ShopItem):
    """
    A Stuffed Animal Item.
    """

    def __init__(self, name, description, product_id, stuffing, size, fabric):
        """

        :param name:
        :param description:
        :param product_id:
        :param stuffing:
        :param size:
        :param fabric:
        """
        super().__init__(name, description, product_id)
        self.stuffing = stuffing
        self.size = size
        self.fabric = fabric

    def __hash__(self):
        return hash((self.name, self.product_id, self.description, self.stuffing, self.size, self.fabric))


class DancingSkeleton(StuffedAnimal):
    """
    Create a Dancing Skeleton.
    """

    def __init__(self, name, product_id, **kwargs):
        super().__init__(name, kwargs["description"], product_id, kwargs["stuffing"],
                         kwargs["size"], kwargs["fabric"])
        self.has_glow = kwargs["has_glow"]

    # def __str__(self):
    #     return f"Name : {self.name}\n" \
    #            f"Product id : {self.product_id}\n" \
    #            f"Stuffing : {self.stuffing}\n" \
    #            f"Size : {self.size}\n" \
    #            f"Fabric : {self.fabric}\n" \
    #            f"Has glow : {self.has_glow}\n"


class Reindeer(StuffedAnimal):
    """
    Create a Reindeer.
    """

    def __init__(self, name, product_id, **kwargs):
        super().__init__(name, kwargs["description"], product_id, kwargs["stuffing"],
                         kwargs["size"], kwargs["fabric"])
        self.has_glow = kwargs["has_glow"]

    # def __str__(self):
    #     return f"Name : {self.name}\n" \
    #            f"Product id : {self.product_id}\n" \
    #            f"Stuffing : {self.stuffing}\n" \
    #            f"Size : {self.size}\n" \
    #            f"Fabric : {self.fabric}\n" \
    #            f"Has glow : {self.has_glow}\n"


class EasterBunny(StuffedAnimal):
    """
    Create an Easter Bunny.
    """

    def __init__(self, name, product_id, **kwargs):
        super().__init__(name, kwargs["description"], product_id, kwargs["stuffing"],
                         kwargs["size"], kwargs["fabric"])
        self.colour = kwargs["colour"]

    # def __str__(self):
    #     return f"Name : {self.name}\n" \
    #            f"Product id : {self.product_id}\n" \
    #            f"Stuffing : {self.stuffing}\n" \
    #            f"Size : {self.size}\n" \
    #            f"Fabric : {self.fabric}\n" \
    #            f"Colour : {self.colour}\n"
