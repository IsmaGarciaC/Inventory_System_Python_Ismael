class Product:
    def __init__(self, name, price, quantity):
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

    def __str__(self):
        return f"{self.name} - ${self.price} (Available: {self.quantity})"

    def update_price(self, new_price):
        new_price.validate_data(new_price):
            self.price = new_price

    def update_quantity(self, new_quantity):
        new_quantity.validate_data(new_quantity):
            self.quantity = new_quantity

    def calculate_total_value(self):
        return self.price * self.quantity




