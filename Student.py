from Person import Person

class Student(Person):
    def __init__(self):
        super().__init__()
        self._fild_of_study = None
        self._year_of_study = None
        self._score_average = None

        self.fild_of_study = input("Enter your fild of study: ")
        self.year_of_study = input("Enter your year of study: ")
        self.score_average = input("Enter your score average: ")
   
    @property
    def fild_of_study(self) -> str:
        return self._fild_of_study
   
    @fild_of_study.setter
    def fild_of_study(self, fild_of_study:str):
        self._fild_of_study = fild_of_study
   
    @property
    def year_of_study(self) -> str:
        return self._year_of_study
   
    @year_of_study.setter
    def year_of_study(self, year_of_study:str):
        self._year_of_study = year_of_study
   
    @property
    def score_average(self) -> str:
        return self._score_average
   
    @score_average.setter
    def score_average(self, score_average:str):
        self._score_average = score_average
    
    
    
    def get_info(self) -> str:
        return super().get_info() + ", fild study: " + self.fild_of_study + ", year study: " + self.year_of_study + ", score average: " + self.score_average

if __name__ == "__main__":
    try:
        print("Testing Student class...")
        student = Student()
        print("Student created successfully!")
        print(student.get_info())
    except ValueError as e:
        print(f"Error during test: {e}") 