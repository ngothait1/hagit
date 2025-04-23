my_person = {}
list_persom = []
avg_age = 0

# Test functions
def checkIndex(index):
    index = int(index)
    if index < 1 or index > 8:
        print("⚠️ The index is not in range")
        return False
    return True
    
def checkDigit(num):
    if not num.isdigit():
        print("⚠️ The value must be a number")
        return False
    return True
   
def isAveilebol(tz, must_exist):
    exists = tz in my_person
    if must_exist and not exists:
        print(f"❌ TZ {tz} does not exist.")
        return False
    if not must_exist and exists:
        print(f"❌ TZ {tz} already exists: {my_person[tz]}")
        return False
    return True

def checkRange(index):
    if(index<0 or index >= len(list_persom)):
        print("❌ Index out of range.")
        return False
    return True

def emptySystem():
    if not my_person:
        print("⚠️ The system is empty")
        return False
    return True


# --------------------------------------------
def saveNewEntry():
    global avg_age
    tz = input("TZ: ")
    if not checkDigit(tz) or not isAveilebol(tz, False):
        return
    name = input("Name: ")
    age = input("Age: ")
    if not checkDigit(age):
        return 
    my_person[tz] = [name,age]        
    avg_age +=int(age)
    list_persom.append(tz)
    print(f"✅ Added: {tz} -> {my_person[tz]}")
 
def searchById():
    if not emptySystem(): return
    tz = input("Enter TZ to search: ")
    if not checkDigit(tz) or not isAveilebol(tz, True): return
    print( f"{tz}:{my_person[tz]}")

def printAgesAverage():
    if not my_person:
        print("Average Age: 0 (no entries)")
    else:
        print (f"Average Age:{avg_age/len(my_person)}")

def printAllNames():
    if not emptySystem(): return
    for index, key in enumerate(my_person):
        print(f"{index+1}. {my_person[key][0]}") 

def printAllIds():
    if not emptySystem(): return
    for index, i in enumerate(list_persom):
        print(f"{index+1}. {i}")

def printAllEntries(): 
    if not emptySystem(): return
    for index, person in enumerate(my_person.items()): 
        print(f"{index}. : {person}" )

def printEntryByIndex():
    if not emptySystem(): return
    index = input("Enter index: ")
    index = int(index)-1
    if not checkRange(index): return
    tz = list_persom[index]
    print(f"{tz}: {my_person[tz]}")

menu_functions = [
    saveNewEntry,
    searchById,
    printAgesAverage,
    printAllNames,
    printAllIds,
    printAllEntries,
    printEntryByIndex]



# -------------------------------------------------
def app():
    choice = 0
    first_time = True
    while True:
        if not first_time:
            input("\n🔁 Press enter to continue")
        first_time = False
        print("""
1. Save a new entry
2. Search by ID
3. Print ages average
4. Print all names
5. Print all IDs
6. Print all entries
7. Print entry by index
8. Exit
""")        
        choice = input("Please enter your choice:")
        if (choice == '8'):
            while (final_exit := input("Are you sure? (y/n): ").lower()) not in {'y', 'n'}:True
            if(final_exit == 'y'):
                print("Goodbye!")
                break
            continue
        elif checkDigit(choice) and checkIndex(choice) :
            menu_functions[int(choice)-1]()
app()
