# Single Inheritance: Base class
class Employee:
    def __init__(self, emp_id, emp_name, emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
    
    def display_employee(self):
        print(f"ID: {self.emp_id}, Name: {self.emp_name}, Salary: ${self.emp_salary}")

# Multilevel Inheritance: Manager inherits from Employee
class Manager(Employee):
    def __init__(self, emp_id, emp_name, emp_salary, department):
        super().__init__(emp_id, emp_name, emp_salary)
        self.department = department

    def display_manager(self):
        self.display_employee()
        print(f"Department: {self.department}")

# Multiple Inheritance: Combines Employee and Benefits
class Benefits:
    def __init__(self, health_insurance, bonus):
        self.health_insurance = health_insurance
        self.bonus = bonus

    def display_benefits(self):
        print(f"Health Insurance: {self.health_insurance}, Bonus: ${self.bonus}")

# Hybrid Inheritance: Combining multiple inheritance classes
class SeniorManager(Manager, Benefits):
    def __init__(self, emp_id, emp_name, emp_salary, department, health_insurance, bonus):
        Manager.__init__(self, emp_id, emp_name, emp_salary, department)
        Benefits.__init__(self, health_insurance, bonus)

    def display_senior_manager(self):
        self.display_manager()
        self.display_benefits()


print("\n----Employee Management System-----")
senior_manager = SeniorManager("E1001", "Usman", 70000, "Finance", "Premium", 5000)
senior_manager.display_senior_manager()



print("\n---------Next one------------")


# Base class: Vehicle
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Hierarchical Inheritance: Different vehicle types inherit from Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors
    
    def car_info(self):
        self.display_info()
        print(f"Number of Doors: {self.num_doors}")

class Bike(Vehicle):
    def __init__(self, brand, model, engine_capacity):
        super().__init__(brand, model)
        self.engine_capacity = engine_capacity
    
    def bike_info(self):
        self.display_info()
        print(f"Engine Capacity: {self.engine_capacity}cc")


print("\n--- Vehicle Management System ---")
car1 = Car("Toyota", "Corolla", 4)
bike1 = Bike("Honda", "CBR", 150)
car1.car_info()
bike1.bike_info()