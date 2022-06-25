class Employee:
    'Records basic employee details.'
    employeeCount = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.id = Employee.employeeCount
        Employee.employeeCount += 1
    
    def displayDetails(self):
        print("Name : ", self.name, "\nID:",self.id, "\nSalary:", self.salary, "\n")
    
    @classmethod
    def displayCount(cls):
        print("Total Employees: ", cls.employeeCount, "\n")
    
    @staticmethod
    def topEarner(employees):
        topEarner = employees[0]
        for employee in employees[1:]:
            if employee.salary > topEarner.salary:
                topEarner = employee
        return topEarner

def main():
    emp1 = Employee("Delboy", 1000)
    emp2 = Employee("Rodney", 600)
    emp3 = Employee("Boycie", 2500)
    employees = [emp1, emp2, emp3]

    emp1.displayDetails()
    emp2.displayDetails()
    emp3.displayDetails()
    Employee.displayCount()
    print("Top earner is:", Employee.topEarner(employees).name,"\n")

if __name__ == '__main__':
    main()
