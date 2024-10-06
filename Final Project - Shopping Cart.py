# Define the ItemToPurchase class
class ItemToPurchase:
    def __init__(self):
        # Default constructor
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    # Method to print item cost
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}')


# Define the ShoppingCart class
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        """Adds an item to the cart."""
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        """Removes an item from the cart by name."""
        item_found = False
        for item in self.cart_items:
            if item['name'].lower().strip() == item_name.lower().strip():  # Ignore case and spaces
                self.cart_items.remove(item)
                item_found = True
                print(f"{item_name} removed from cart.")
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item):
        """Modifies an item’s description, price, or quantity."""
        item_found = False
        for item in self.cart_items:
            if item['name'].lower().strip() == modified_item['name'].lower().strip():  # Ignore case and spaces
                if modified_item['description'] != "none":
                    item['description'] = modified_item['description']
                if modified_item['price'] != 0:
                    item['price'] = modified_item['price']
                if modified_item['quantity'] != 0:
                    item['quantity'] = modified_item['quantity']
                item_found = True
                print(f"{modified_item['name']} has been updated.")
                break
        if not item_found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        """Returns total number of items in the cart."""
        return sum(item['quantity'] for item in self.cart_items)

    def get_cost_of_cart(self):
        """Calculates and returns the total cost of the cart."""
        total_cost = 0
        for item in self.cart_items:
            total_cost += item['price'] * item['quantity']
        return total_cost

    def print_total(self):
        """Prints the total cost of the shopping cart."""
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                print(f"{item['name']} {item['quantity']} @ ${item['price']} = ${item['quantity'] * item['price']}")
            print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        """Prints descriptions of each item in the cart."""
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print("Item Descriptions")
            for item in self.cart_items:
                print(f"{item['name']}: {item['description']}")


# Define the menu function to handle cart operations
def print_menu(cart):
    """Displays a menu of options and handles user input."""
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ").lower()

        if choice == 'a':
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            price = float(input("Enter item price: $"))
            quantity = int(input("Enter item quantity: "))
            item = {'name': name, 'description': description, 'price': price, 'quantity': quantity}
            cart.add_item(item)
        elif choice == 'r':
            name = input("Enter the name of the item to remove: ")
            cart.remove_item(name)
        elif choice == 'c':
            name = input("Enter the name of the item to modify: ")
            description = input("Enter the new description (or 'none' to leave unchanged): ")
            price = float(input("Enter the new price (or 0 to leave unchanged):$ "))
            quantity = int(input("Enter the new quantity (or 0 to leave unchanged): "))
            modified_item = {'name': name, 'description': description, 'price': price, 'quantity': quantity}
            cart.modify_item(modified_item)
        elif choice == 'i':
            cart.print_descriptions()
        elif choice == 'o':
            cart.print_total()
        elif choice == 'q':
            break
        else:
            print("Invalid option, try again.")


# Main function to initialize and start the shopping cart program
def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)


# Execute the main function
if __name__ == "__main__":
    main()
