from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


class CoffeeMachine:
    def __init__(self):
        self.water = 1000
        self.milk = 1000
        self.sugar = 100
        self.money = 0

    def place_order(self):
        clear()
        print("\nPlace Order")
        coffee = self.choose_type()
        clear()
        print(f"You chose {coffee.name}")
        transaction_success = self.collect_money(coffee.cost)
        if not transaction_success:
            print("\nSorry order could not process")
            return
        print("Order Placed Successfully\n")
        order_success = self.prepare_order(coffee)
        if not order_success:
            print(f"\nSorry order could not process your order. Here is a refund of Rs.{coffee.cost}")
            self.money -= coffee.cost
            return
        print(f"Order Prepared. Here is your {coffee.name}")

    def choose_type(self):
        clear()
        loop = 0
        coffee_type = None
        while loop == 0:
            print("Choose Type of Coffee\n1)Espresso\n2)Latte\n3)Cappuccino\n")
            option = int(input("-> "))
            if option == 1:
                coffee_type = Espresso()
                loop = 1
            elif option == 2:
                coffee_type = Latte()
                loop = 1
            elif option == 3:
                coffee_type = Capuccino()
                loop = 1
            else:
                print("Wrong Option. Please Choose Again\n")
                loop = 0
        return coffee_type

    def collect_money(self, coffee_cost):
        print(f"\nYour Total is {coffee_cost}\n")
        total = 0
        note_100 = abs(int(input("Number of Rs.100 Note: ")))
        note_50 = abs(int(input("Number of Rs.50 Note: ")))
        note_20 = abs(int(input("Number of Rs.20 Note: ")))
        total = total + ((100 * note_100) + (50 * note_50) + (20 * note_20))
        clear()
        print(f"Total money inserted: Rs.{total}\n")
        if total == coffee_cost:
            self.money += total
        elif total > coffee_cost:
            self.money += total
            balance = total - coffee_cost
            print(f"Here is you Rs.{balance} change")
            self.money -= balance
        else:
            balance = coffee_cost - total
            print(f"Not Enough Money. Add Rs.{balance} more\nHere is you Rs.{total} back")
            return False
        return True

    def prepare_order(self, coffee_type):
        print(f"Preparing {coffee_type.name}\n")
        success = coffee_type.make_coffee(self.water, self.milk, self.sugar)
        if not success:
            return False
        self.water -= coffee_type.water_required
        self.milk -= coffee_type.milk_required
        self.sugar -= coffee_type.sugar_required
        return True

    def show_report(self):
        print("\nCoffee Machine Report")
        print(f"Water: {self.water} ml")
        print(f"Milk: {self.milk} ml")
        print(f"Sugar: {self.sugar} g")
        print(f"Money Collected: Rs. {self.money}")

    def refill(self):
        if self.money >= 10:
            print("Refilling the Coffee Machine with Supplies")
            self.money -= 10
            self.water += 1000
            self.milk += 1000
            self.sugar += 100
        else:
            print("Not Enough money to refill")


class Coffee:
    def __init__(self, water_required, milk_required, sugar_required, cost):
        self.water_required = water_required
        self.milk_required = milk_required
        self.sugar_required = sugar_required
        self.cost = cost

    def make_coffee(self, water, milk, sugar):
        if water < self.water_required or milk < self.milk_required or sugar < self.sugar_required:
            print("Not Enough Supplies. Please ask Barista to REFILL\n")
            return False
        return True


class Espresso(Coffee):
    def __init__(self):
        super().__init__(300, 0, 0, 200)
        self.name = "Espresso"


class Latte(Coffee):
    def __init__(self):
        super().__init__(0, 300, 30, 250)
        self.name = "Latte"


class Capuccino(Coffee):
    def __init__(self):
        super().__init__(100, 200, 20, 300)
        self.name = "Capuccino"


if __name__ == '__main__':
    clear()
    coffee_machine = CoffeeMachine()
    print("Welcome to AD's Virtual Coffee Experience\n")
    choice = 0
    while choice != 2:
        print("\nWhat would you like today?\n1)Place an Order\n2)Exit Coffee Experience\n")
        choice = int(input("-> "))
        if choice == 1:
            # Give options for coffee
            coffee_machine.place_order()
        elif choice == 2:
            print("Thank you for Visiting!!\n")
            exit(0)
        elif choice == 3:
            # Show Report
            coffee_machine.show_report()
        elif choice == 4:
            coffee_machine.refill()
        else:
            print("Please Choose a valid option\n\n")
