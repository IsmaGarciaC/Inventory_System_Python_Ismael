#Class Product
class Product:
    def __init__(self, name, price, quantity):

        # Initialize the product with name, price, and quantity
        self.validate_data(name, price, quantity)
        self.name = name
        self.price = price
        self.quantity = quantity

    def validate_data(self, name, price, quantity):
        if not isinstance(name, str) or not isinstance(price, float) or not isinstance(quantity, int):
            raise ValueError("Invalid input types. Name should be a string, price should be a float, and quantity should be an integer.")
        if name == "":
            raise ValueError("The product name cannot be empty.")
        if price < 0:
            raise ValueError("Price should be non-negative.")
        if quantity < 0:
            raise ValueError("Quantity should not be negative.")

    # Method to display product details
    def __str__(self):
        return f"{self.name} - ${self.price} (Available: {self.quantity})"

    def update_price(self, new_price):
        if new_price < 0:
            raise ValueError("Price should be non-negative.")
        self.price = new_price

    def update_quantity(self, new_quantity):
        if new_quantity < 0:
            raise ValueError("Quantity should not be negative.")
        self.quantity = new_quantity

    def calculate_total_value(self):
        return self.price * self.quantity

class Inventory:
    def __init__(self): 
        # Initialize an empty list to store products
        self.products = []

    def add_product(self, product):
        # Add a product to the inventory
        if not isinstance(product, Product):
            raise ValueError("Invalid product type. Expected a Product object.")
        self.products.append(product)

    def remove_product(self, name):
        # Remove a product from the inventory by name
        for i, product in enumerate(self.products):
            if product.name == name:
                del self.products[i]
                return True
        return False

    def search_product(self, name):
        # Get a product by its name
        for product in self.products:
            if product.name == name:
                return product
        return None

    def list_products(self):
        # List all products in the inventory
        for product in self.products:
            print(product)

    def calculate_inventory_value(self):
        total_value = 0
        for product in self.products:
            total_value += product.calculate_total_value()
        return total_value

def main_menu(inventory):
    while True:
        print("Inventory Management System")
        print("-"*30)
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Search Product")
        print("4. List Products")
        print("5. Calculate Inventory Value")
        print("6. Exit")
        print("-"*30)

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                name = input("Product Name: ")
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))
                product = Product(name, price, quantity)
                inventory.add_product(product)
                print(f"Product '{name}' added successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            name = input("Product Name to Remove: ")
            if inventory.remove_product(name):
                print(f"Product '{name}' removed successfully.")
            else:
                print(f"Product '{name}' not found in the inventory.")

        elif choice == '3':
            name = input("Product Name to Search: ")
            product = inventory.search_product(name)
            if product:
                print(product)
            else:
                print(f"Product '{name}' not found in the inventory.")

        elif choice == '4':
            inventory.list_products()

        elif choice == '5':
            total_value = inventory.calculate_inventory_value()
            print(f"Total Inventory Value: ${total_value:.2f}")

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    inventory = Inventory()
    main_menu(inventory)
