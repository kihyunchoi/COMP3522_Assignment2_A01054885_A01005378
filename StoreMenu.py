class Store:
    """
    The Store class.
    """
    def __init__(self):
        self.inventory = {} # product_id as key

    def receive_orders(self):
        print("Receiving Orders")

    def get_item(self):
        print("Getting item")

    def daily_transaction_report(self):
        print("Daily transaction report...")


class Menu:
    """
    The UI interface for the Store.
    """

    def __init__(self):
        self.store = Store()

    def show_menu(self):
        print("-" * 50)
        print("Welcome to the Holiday Store's Inventory System")
        print("-" * 50)
        print("1. Process Web Orders")
        print("2. Check Inventory")
        print("3. Exit")

def main():
    shop = Menu()
    shop.show_menu()

if __name__ == '__main__':
    main()