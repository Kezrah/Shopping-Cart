class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, item):
        self.cart.append(item)
        print(item, "added to cart.")

    def remove_item(self, item):
        if item in self.cart:
            self.cart.remove(item)
            print(item, "removed from cart.")
        else:
            print("Item not found.")

    def view_cart(self):
        if len(self.cart) == 0:
            print("Cart is empty.")
        else:
            print("Items in cart:")
            for item in self.cart:
                print("-", item)

    def checkout(self):
        print("Checking out...")
        print("Items bought:", self.cart)
        print("Thank you for shopping!")


cart = ShoppingCart()

while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        item = input("Enter item name: ")
        cart.add_item(item)

    elif choice == "2":
        item = input("Enter item to remove: ")
        cart.remove_item(item)

    elif choice == "3":
        cart.view_cart()

    elif choice == "4":
        cart.checkout()
        break

    elif choice == "5":
        break

    else:
        print("Invalid choice.")
