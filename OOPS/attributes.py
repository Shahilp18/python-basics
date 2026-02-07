
#! Attributes: Class & Instance
#* class : belong to class + commmon | eg.. college name  
#* instance: belong to object + unique | eg.. name,cgpa,subject

class Bank:
    bank_name = "SBI Bank"

    def __init__(self, cus_name, branch):
        self.cus_name = cus_name
        self.branch = branch

b1 = Bank("Shahil Patel", "Navrangpura")
print(b1.cus_name, b1.branch)
print(Bank.bank_name)




