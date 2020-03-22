import datetime

from file_handler import FileHandler
from oerder_processor import OrderProcessor


class Store:
    """
    The Store class.
    """

    def __init__(self):
        self.inventory = {}  # product_id as key

    def receive_orders(self):
        # print("Receiving Orders")

        # file_name = input("Enter an excel fileName: ")
        # self.inventory = OrderProcessor.read_file(file_name + ".xlsx")

        orders = OrderProcessor.read_file("orders.xlsx")
        for i in orders:
            print(i)

    def get_item(self):
        print("Getting item")

    def check_inventory(self):
        print("Check Inventory")

    def daily_transaction_report(self):
        now = datetime.datetime.now()
        report_date = now.strftime("%d%m%Y")
        report_time = now.strftime("%H%M")
        file_name = "DTR_" + report_date + "_" + report_time + ".txt"
        lines = ["HOLIDAY STORE - DAILY TRANSACTION REPORT (DTR)", now.strftime("%d-%m-%Y %H:%M")]
        # print(file_name)
        # FileHandler.write_lines(file_name, lines)
        # FileHandler.load_data(file_name)
        FileHandler.load_data("DTR_21032020_0635.txt")
        # print("\nHOLIDAY STORE - DAILY TRANSACTION REPORT (DTR)")
        # print(now.strftime("%d-%m-%Y %H:%M"))


class Menu:
    """
    The UI interface for the Store.
    """

    def __init__(self):
        self.store = Store()

    def show_menu(self):
        user_input = None
        while user_input != 3:
            print("-" * 50)
            print("Welcome to the Holiday Store's Inventory System")
            print("-" * 50)
            print("1. Process Web Orders")
            print("2. Check Inventory")
            print("3. Exit")
            user_input = int(input("Please enter your choice (1- 3)"))

            if user_input == 1:
                self.store.receive_orders()
            elif user_input == 2:
                self.store.check_inventory()
            elif user_input == 3:
                self.store.daily_transaction_report()
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 3.")


def main():
    shop = Menu()
    shop.show_menu()


if __name__ == '__main__':
    main()
