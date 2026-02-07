
#! Product store 
"""
Design & create an online store for Products(name, price).

Track total products being created

Create a static method to calculate discount on each product based on a % parameter
"""

class Product:
    count = 0;
    product_type = "Electronics"

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count+=1

    def get_product(self): #? instance
        print(f"Product is {self.name} & price is {self.price}")

    @classmethod
    def get_count(cls):
        print(f"Product Count = {cls.count}")

    @staticmethod
    def calc_disc(price, discount):
        print(f"Discounted price = {price - (price * discount / 100)}")

       

p1 = Product("iPhone 17", 1_50_000)
p2 = Product("macbook pro", 2_00_000)
p1.calc_disc(p1.price, 50)
Product.get_count()

p1.get_product()
p2.get_product()
