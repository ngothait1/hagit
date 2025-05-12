from Validators import check_digit, is_available, is_not_available
class Person:
    def __init__(self):
        self._TZ = None  
        self._name = None
        self._age = None
              
        self.TZ = input("Enter your TZ: ")
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
 
    @property
    def TZ(self) -> str:
        return self._TZ
    
    @TZ.setter
    def TZ(self, TZ:str):
            check_digit(TZ) 
            self._TZ = TZ

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name:str):
        if not name:
            raise ValueError("Name cannot be empty")
        if not name.isalpha():
            raise ValueError("Name must contain only letters")
        self._name = name

    @property  
    def age(self)-> str:
        return self._age
    
    @age.setter
    def age(self, age:str):
            check_digit(age)
            self._age = age

    def get_info(self) -> str:
        return f"TZ: {self.TZ} Name: {self.name}, Age: {self.age}"

if __name__ == "__main__":
    try:
        print("Testing Person class...")
        person = Person()
        print("Person created successfully!")
        print(person.get_info())
    except ValueError as e:
        print(f"Error during test: {e}")
        