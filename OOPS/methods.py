
#! Methods
#* instance, class, static methods

class Laptop:
    storage_type = "SSD"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod  #? class method  @decorator
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type} ")

    def get_info(self): #? instance method
        print(f"Laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

    @staticmethod #? static method  @decorator
    def  calc_discount(price, discount):
        final_price = price - (discount * price / 100)
        print(f"discounted price = {final_price}")

l1 = Laptop("16gb", "512gb")
l1.calc_discount(40_000, 10)
 
Laptop.get_storage_type()

l1.get_info()



