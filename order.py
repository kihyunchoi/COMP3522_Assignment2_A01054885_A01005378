class Order:
    """
    Create an order for the shop.
    """
    def __init__(self, order_number, product_id, item, name, quantity, product_details, factory):
        self._order_number = order_number
        self._product_id = product_id
        self._item = item
        self._name = name
        self._quantity = quantity
        self._product_details = product_details
        self._factory = factory

    @property
    def order_number(self):
        return self._order_number

    @property
    def product_id(self):
        return self._product_id

    @property
    def item(self):
        return self._item

    @property
    def name(self):
        return self._name

    @property
    def quantity(self):
        return self._quantity

    @property
    def product_details(self):
        return self._product_details

    @property
    def factory(self):
        return self._factory

    def __str__(self):
        return f"Order number : {self.order_number}\n" \
               f"Product id : {self.product_id}\n" \
               f"Item : {self.item}\n" \
               f"Name : {self.name}\n" \
               f"Quantity : {self.quantity}\n" \
               f"Product Details : {self.product_details}\n"
