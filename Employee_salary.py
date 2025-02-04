class Employee_details:
    def _init_(self, name, id):
        self.name=name
        self.id=id

    def show(self, salary):
        print(f"Name: {self.name:15} \nEmployee Id: {self.id}\n")
        print(f"Salary Rupees {salary}")

class developer(Employee_details):
    def _init_(self, name, id):
        self.salary = 70000
        super()._init_(name, id)
        super().show(self.salary)

class Administrator(Employee_details):
    def _init_(self, name, id):
        self.salary = 55000
        super()._init_(name, id)
        super().show(self.salary)  

class HR(Employee_details):
    def _init_(self, name, id):
        self.salary = 40000
        super()._init_(name, id)
        super().show(self.salary)

user_1 = developer("Krithika", 12345678)
user_2 = HR("Swetha", 987654321)