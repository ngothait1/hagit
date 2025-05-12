import os
from typing import Dict, List
import pandas as pd
from Action import Action
from Person import Person
from Employee import Employee
from Student import Student
from Validators import check_digit, is_available, is_not_available, check_range, empty_system, check_range_option

def saveNewEntry(persons: dict[str, Person], persons_ids, sum_age):
    print("please enter the following details:")
    new_person_options = {
        '1': ["regular man",lambda:Person()],
        '2': ["Student", lambda:Student()],
        '3': ["Employee",lambda:Employee()],
    }
    print("Select the type of user you want to add:")
    for key, value in new_person_options.items():
        print(f"{key}. {value[0]}")
        
    choice = input("Enter your choice: ")
    try:
        check_digit(choice) 
        check_range_option(choice, new_person_options)
        new_user = new_person_options[choice][1]()
        is_available(new_user.TZ, persons)
        persons[new_user.TZ] = new_user
        sum_age[0] += int(new_user.age)
        persons_ids.append(new_user.TZ)
        print(f"Added: {new_user.get_info()}")
    except ValueError as e:
        print(f"Error: {e}")

def searchById(persons: dict[str, Person]) -> str:
    try:
        empty_system(persons)
        tz = input("Enter TZ to search: ")
        check_digit(tz)
        is_not_available(tz, persons)
        print(persons[tz].get_info())
    except ValueError as e:
        print(f"Error: {e}")
        
def printAgesAverage(persons: dict[str, Person], sum_age):
    if not persons:
        print("Average Age: 0 (no entries)")
    else:
        print (f"Average Age:{sum_age[0]/len(persons)}")

def printAllNames(persons: dict[str, Person]):
    try:
        empty_system(persons)
        for index, person in enumerate(persons.values()):
            print(f"{index + 1}. {person.name}")
    except ValueError as e:
        print(f"Error: {e}")

def printAllIds(persons_ids):
    try:
        empty_system(persons_ids)
        for index, person_id in enumerate(persons_ids):
            print(f"{index + 1}. {person_id}") 
    except ValueError as e:
        print(f"Error: {e}")

def printAllEntries(persons: dict[str, Person]):  
    try:
        empty_system(persons)
        for index, person in enumerate(persons.values()):
            print(f"{index + 1}. : {person.get_info()}" )
    except ValueError as e:
        print(f"Error: {e}")

def printEntryByIndex(persons: dict[str, Person], persons_ids:list[str]):
    try:
        empty_system(persons)
        index = input("Enter index: ")
        check_digit(index)
        index = int(index) - 1
        check_range(index, persons_ids)
        tz = persons_ids[index]
        print(persons[tz].get_info())
    except ValueError as e:
        print(f"Error: {e}")

def saveAllData(persons: dict[str, Person]):
    try:
        empty_system(persons)
        data = []
        # replace the object to list
        all_keys = set()
        for key, values in persons.items():
            all_keys.update(values.__dict__.keys())
            data.append(values.__dict__)

        all_keys = list(all_keys) 
        df = pd.DataFrame(data, columns=all_keys)
        name_file = input("Enter file name: ")
        if not name_file.endswith('.csv'):
            name_file += '.csv'
        df.to_csv(name_file, index=False)
        print("Data saved successfully!")
    except ValueError as e:
        print(f"Error: {e}")    

def app():
        choice = 0
        first_time = True
        persons: Dict[str, Person] = {}
        persons_ids: List[str] = []
        sum_age = [0]
        actions = {
        Action.SAVE_NEW_ENTRY: ["Save a new entry", lambda: saveNewEntry(persons, persons_ids, sum_age)],
        Action.SEARCH_BY_ID: ["Search by ID", lambda: searchById(persons)],
        Action.PRINT_AGES_AVERAGE: ["Print ages average", lambda: printAgesAverage(persons, sum_age)],
        Action.PRINT_ALL_NAMES: ["Print all names", lambda: printAllNames(persons)],
        Action.PRINT_ALL_IDS: ["Print all IDs", lambda: printAllIds(persons_ids)],
        Action.PRINT_ALL_ENTRIES: ["Print all entries", lambda: printAllEntries(persons)],
        Action.PRINT_ENTRY_BY_INDEX: ["Print entry by index", lambda: printEntryByIndex(persons, persons_ids)],
        Action.SAVE_ALL_DATA: ["Save all data", lambda: saveAllData(persons)],
        Action.EXIT: ["Exit", lambda: exit()]
        }
        while True:
            try:
                for number in actions:
                    print(F"{number.value}. {actions[number][0]}")
                if not first_time:
                    input("\n Press enter to continue")
                first_time = False
                choice = input("Please enter your choice:")
                check_digit(choice)
                choice = int(choice) 
                if choice == Action.EXIT.value:
                    while (final_exit := input("Are you sure? (y/n): ").lower()) not in {'y', 'n'}:True
                    if(final_exit == 'y'):
                        print("Goodbye!")
                        break
                    continue
                if choice not in [action.value for action in Action]:
                    print("Invalid choice! Please enter a number between 1 and 9.")
                    continue
                choice = Action(choice)
                print(actions[choice][0])
                actions[choice][1]()

            except ValueError as e:
                print(f"Error: {e}")  
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break                
if __name__ == "__main__":            
    app()
