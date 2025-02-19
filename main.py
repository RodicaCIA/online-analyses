from cart import Cart
from produse import Product
from produse_manager import ProductManager

manager = ProductManager()

# Adăugare produse
manager.add_product(Product("Laptop", 3000, 5))
manager.add_product(Product("Mouse", 150, 10))
manager.add_product(Product("Keyboard", 250, 7))

# Afișare produse și valoare totală
manager.display_products()
print(f"Total Inventory Value: {manager.total_inventory_value()}")

def remove_product(self, name):
    self.products = [product for product in self.products if product.name != name]

    from cart import Cart

cart = Cart()

# Adăugare produse în coș
cart.add_to_cart(manager.products[0])
cart.add_to_cart(manager.products[1])
cart.add_to_cart(manager.products[2])

cart.display_cart()
print(f"Total Cart Value: {cart.total_cart_value()}")