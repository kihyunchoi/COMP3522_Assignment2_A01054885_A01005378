from ShopItem import ShopItem


class Candy(ShopItem):
    """
    A Candy that the store stocks.
    """

    def __init__(self, name, description, product_id, has_nuts, has_lactose):
        """
        Create a Candy item.
        :param name:
        :param description:
        :param product_id:
        :param has_nuts:
        :param has_lactose:
        """
        super().__init__(name, description, product_id)
        self.has_nuts = has_nuts
        self.has_lactose = has_lactose


class PumpkinCaramelToffee(Candy):
    """
    Create a Pumpkin Caramel Toffee item.
    """

    def __init__(self, **kwargs):
        super().__init__(kwargs["name"], kwargs["description"], kwargs["product_id"],
                         kwargs["has_nuts"], kwargs["has_lactose"])
        self.variety = kwargs["variety"]

    # def __str__(self):
    #     return f"Name : {self.name}\n" \
    #            f"Product id : {self.product_id}\n" \
    #            f"Has nuts : {self.has_nuts}\n" \
    #            f"Has lactose : {self.has_lactose}\n" \
    #            f"Variety : {self.variety}\n"


class CandyCanes(Candy):
    """
    Create Candy Cane item.
    """

    def __init__(self, **kwargs):
        super().__init__(kwargs["name"], kwargs["description"], kwargs["product_id"],
                         kwargs["has_nuts"], kwargs["has_lactose"])
        self.colour = kwargs["colour"]

    # def __str__(self):
    #     return f"Name : {self.name}\n" \
    #            f"Product id : {self.product_id}\n" \
    #            f"Has nuts : {self.has_nuts}\n" \
    #            f"Has lactose : {self.has_lactose}\n" \
    #            f"Colour : {self.colour}\n"


class CremeEggs(Candy):
    """
    Create Creme Eggs.
    """

    def __init__(self, **kwargs):
        super().__init__(kwargs["name"], kwargs["description"], kwargs["product_id"],
                         kwargs["has_nuts"], kwargs["has_lactose"])
        self.pack_size = kwargs["pack_size"]

    # def __str__(self):
    #     return f"Name : {self.name}\n" \
    #            f"Product id : {self.product_id}\n" \
    #            f"Has nuts : {self.has_nuts}\n" \
    #            f"Has lactose : {self.has_lactose}\n" \
    #            f"Pack size : {self.pack_size}\n"
