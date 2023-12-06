class HamburguerJoint:
    def __init__(self):
        self.menu = {
            "Plain Burger": 5.99,
            "Cheeseburger": 6.99,
            "Double Burger": 7.99,
            "Special Burger": 8.99,
            "French Fries": 2.99,
            "Soda": 1.99
        }
        self.order = {}

    def show_menu(self):
        print("---- Menu ----")
        for item, price in self.menu.items():
            print(f"{item}: ${price}")

    def take_order(self):
        while True:
            self.show_menu()
            print("Type 'done' to finish the order.")
            product = input("Choose a product: ")
            if product.lower() == 'done':
                break
            if product in self.menu:
                quantity = int(input(f"Quantity of '{product}': "))
                if product in self.order:
                    self.order[product] += quantity
                else:
                    self.order[product] = quantity
            else:
                print("Invalid product. Please choose a product from the menu.")

    def calculate_total(self):
        total = 0
        print("\n---- Order ----")
        for product, quantity in self.order.items():
            price = self.menu[product]
            subtotal = price * quantity
            print(f"{product}: {quantity} x ${price} = ${subtotal:.2f}")
            total += subtotal
        return total

    def run(self):
        print("Welcome to the Hamburguer Joint!")
        self.take_order()
        total = self.calculate_total()
        print(f"\nTotal amount to pay: ${total:.2f}")
        print("Thank you for your purchase!")

# Program usage
hamburguer_joint = HamburguerJoint()
hamburguer_joint.run()
