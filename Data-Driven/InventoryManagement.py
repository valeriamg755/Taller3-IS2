class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.name not in self.products:
            self.products[product.name] = product
        else:
            print("Product already exists in inventory.")

    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
        else:
            print("Product not found in inventory.")

    def update_product_quantity(self, product_name, new_quantity):
        if product_name in self.products:
            self.products[product_name].update_quantity(new_quantity)
        else:
            print("Product not found in inventory.")

    def list_products(self):
        print("Current Inventory:")
        for product in self.products.values():
            print(f"{product.name}: ${product.price} - Quantity: {product.quantity}")


if __name__ == "__main__":
    inventory = Inventory()

    inventory.add_product(Product("Book", 100000, 10))
    inventory.add_product(Product("Plushie", 80000, 50))
    inventory.add_product(Product("Snack", 10000, 30))

    inventory.list_products()

    inventory.update_product_quantity("Plushie", 25)

    inventory.list_products()

    inventory.remove_product("Snack")

    inventory.list_products()
