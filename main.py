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