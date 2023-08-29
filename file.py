class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []
        
    def add_employee(self, emp):
        self.employees.append(emp)
        
    def search_by_age(self, age):
        result = [emp for emp in self.employees if emp.age == age]
        return result
        
    def search_by_name(self, name):
        result = [emp for emp in self.employees if emp.name == name]
        return result
        
    def search_by_salary(self, operator, amount):
        if operator == "<":
            result = [emp for emp in self.employees if emp.salary < amount]
        elif operator == ">":
            result = [emp for emp in self.employees if emp.salary > amount]
        elif operator == "<=":
            result = [emp for emp in self.employees if emp.salary <= amount]
        elif operator == ">=":
            result = [emp for emp in self.employees if emp.salary >= amount]
        else:
            result = []
        return result
        
def main():
    emp_db = EmployeeDatabase()
    
    emp_db.add_employee(Employee("161E90", "Raman", 41, 56000))
    emp_db.add_employee(Employee("161F91", "Himadri", 38, 67500))
    emp_db.add_employee(Employee("161F99", "Jaya", 51, 82100))
    emp_db.add_employee(Employee("171E20", "Tejas", 30, 55000))
    emp_db.add_employee(Employee("171G30", "Ajay", 45, 44000))
    
    print("Search options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (<, >, <=, >=)")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        age = int(input("Enter age to search: "))
        result = emp_db.search_by_age(age)
    elif choice == 2:
        name = input("Enter name to search: ")
        result = emp_db.search_by_name(name)
    elif choice == 3:
        operator = input("Enter operator (<, >, <=, >=): ")
        amount = int(input("Enter amount: "))
        result = emp_db.search_by_salary(operator, amount)
    else:
        print("Invalid choice")
        return
        
    if result:
        print("Search results:")
        for emp in result:
            print(f"ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
    else:
        print("No matching records found.")

if __name__ == "__main__":
    main()
