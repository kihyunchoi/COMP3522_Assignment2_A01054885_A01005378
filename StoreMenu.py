import datetime

from file_handler import FileHandler
from order_processor import OrderProcessor


class Store:
    """
    The Store class.
    """

    def __init__(self):
        self.inventory = {}
        self.orders = []

    def receive_orders(self):
        """
        Get orders from excel sheet and process them in store.
        """
        print("-" * 50)
        print("Receiving Orders")
        print("-" * 50)

        file_name = input("Enter an excel fileName: ")
        temp_orders = OrderProcessor.read_file(file_name + ".xlsx")
        self.orders.extend(OrderProcessor.read_file(file_name + ".xlsx"))
        for i in temp_orders:
            print("Processing order {}".format(i.order_number))
            factory = i.factory
            name = i.name
            product_id = i.product_id
            details = i.product_details

            functions = {"Toy": factory().create_toy,
                         "Candy": factory().create_candy,
                         "StuffedAnimal": factory().create_stuffed_animal}

            item = functions[i.item](name=name, product_id=product_id, **details)
            validation = {"Toy": OrderProcessor.validate_toy_order,
                          "Candy": OrderProcessor.validate_candy_order,
                          "StuffedAnimal": OrderProcessor.validate_stuffed_order}
            validate = validation[i.item]
            if item not in self.inventory.keys() and len(validate(i)) == 0:
                self.inventory[item] = 100 - i.quantity
            elif len(validate(i)) == 0:
                self.inventory[item] = self.inventory[item] - i.quantity

    def check_inventory(self):
        """
        Display the inventory and the status of a specific item.
        :return:
        """
        print("-" * 50)
        print("Inventory")
        print("-" * 50)
        if len(self.inventory) == 0:
            print("Empty inventory")
        else:
            for key, quant in self.inventory.items():
                if quant >= 10:
                    print("{}: {} - In stock".format(key.name, quant))
                elif 10 > quant >= 3:
                    print("{}: {} - Low".format(key.name, quant))
                elif 3 > quant > 0:
                    print("{}: {} - Very Low".format(key.name, quant))
                else:
                    print("{}: {} - Out of stock".format(key.name, quant))
        print("")

    def daily_transaction_report(self):
        """
        Save the daily transactions to a file with the time and date of generation.
        """
        now = datetime.datetime.now()
        report_date = now.strftime("%d%m%Y")
        report_time = now.strftime("%H%M")
        file_name = "DTR_" + report_date + "_" + report_time + ".txt"
        lines = ["HOLIDAY STORE - DAILY TRANSACTION REPORT (DTR)", now.strftime("%d-%m-%Y %H:%M")]
        print("Saving Daily Transaction Report to {}".format(file_name))
        try:
            with open(file_name, mode="w") as file:
                for row in lines:
                    file.write(str(row) + "\n")

                file.write("\n")
                for order in self.orders:
                    order_num = order.order_number
                    item = order.item
                    product_id = order.product_id
                    name = order.name
                    quantity = order.quantity
                    validation = {"Toy": OrderProcessor.validate_toy_order,
                                  "Candy": OrderProcessor.validate_candy_order,
                                  "StuffedAnimal": OrderProcessor.validate_stuffed_order}
                    validate = validation[order.item]
                    error = validate(order)
                    if len(error) == 0:
                        string = "Order {}, Item {}, Product ID {}, Name \"{}\", Quantity {}".format(order_num, item,
                                                                                                     product_id, name,
                                                                                                     quantity)
                    else:
                        string = "Order {}, Could not process order data was corrupted, " \
                                 "InvalidDataError - {}".format(order_num, error)
                    file.write(string + "\n")
        except FileNotFoundError:
            print("Could not print out daily transaction report.")


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
            try:
                user_input = int(input("Please enter your choice (1- 3): "))

                if user_input == 1:
                    self.store.receive_orders()
                elif user_input == 2:
                    self.store.check_inventory()
                elif user_input == 3:
                    self.store.daily_transaction_report()
                else:
                    print("Could not process the input. Please enter a"
                          " number from 1 - 3.\n")
            except ValueError:
                print("Could not process the input. Please enter a number from 1 - 3.\n")


def main():
    shop = Menu()
    shop.show_menu()


if __name__ == '__main__':
    main()
