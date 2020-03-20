import abc


class ShopItem(abc.ABC):
    """
    An item the shop can stock.
    """

    def __init__(self, name, description, product_id):
        self.name = name
        self.description = description
        self.product_id = product_id
