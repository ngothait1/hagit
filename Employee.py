from  Person import Person

class Employee(Person):
    def __init__(self):
        super().__init__()
        self._position = None
        self._salary = None
        self.position = input("Enter your position: ")
        self.salary = input("Enter your salary: ")

    @property
    def position(self) -> str:
        return self._position
    
    @position.setter
    def position(self, position:str):
        self._position = position
    
    @property
    def salary(self) -> str:
        return self._salary
    
    @salary.setter
    def salary(self, salary:str):
        self._salary = salary

    def get_info(self) -> str:
        return super().get_info() + ", Position: " + self.position + ", Salary: " + self.salary
    
if __name__ == "__main__":
    try:
        print("Testing Employee class...")
        employee = Employee()
        print("Employee created successfully!")
        print(employee.get_info())
    except ValueError as e:
        print(f"Error during test: {e}")