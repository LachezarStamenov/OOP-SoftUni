# In the product_repository.py file, the class ProductRepository should be implemented. It is a repository for all
# products that are delivered to the grocery shop.
# The class should have products: list - an empty list, which will be containing all products (objects). Also, .
# the class should have 4 additional methods:
# •	add(product: Product) - adds a product to the repository
# •	find(product_name: str) - returns a product (object) with that name
# •	remove(product_name) - removes a product from the repository
# •	__repr__() - override the method, so it returns information for all products in the repository:
# "{product_name1}: {quantity1}"
# {product_name2}: {quantity2}
# …
# {product_nameN}: {quantityN}"

from .product import Product

class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.__name == product_name:
                return product

    def remove(self, product_name):
        for product in self.products:
            if product.__name == product_name:
                self.products.remove(product)

    def __repr__(self):
        result = ''
        for product in self.products:
            result += f'{product.__name}: {product.quantity}\n'
        return result.strip()
