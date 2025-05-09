import json

def read_data():
    try:
        with open ("students.json") as file:
            students=json.load(file)
            return students
    except FileNotFoundError:
        return[]
          
def write_data(students):
    with open("students.json","w") as file:
        json.dump(students,file,indent=4)
        
  

def add_student():
    students = read_data()    
    roll_no = [student["roll_no"] for student in students]

    roll_number=input("Enter roll_no:")
   
          
    if roll_number in roll_no:
        print("Student with this roll number already exists.")
        return
    name=input("Enter name:\n")
    try:
        physics=int(input("Enter Physics marks:"))
        chemistry=int(input("Enter chemistry marks:"))
        maths=int(input("Enter maths marks:"))
    except ValueError:
        print("Invalid input. Marks should be integers")
        return
    students.append({
        'name':name,
        'roll_no':roll_number,
        'marks':{
            'physics':physics,
            'chemistry':chemistry,
            'maths':maths
        }
    })
    
    write_data(students)
    print("students added successfully")
    
def display_all_students():
    students = read_data()
    if not students:
        print("No students to display")
        return
    print("\n All students")
    for student in students:
        print("Name:",student['name'])
        print("roll_no:",student['roll_no'])
        print("Marks:")
        print("Physics:",student['marks']['physics'])
        print("Chemistry:",student['marks']['chemistry'])
        print("Maths:",student['marks']['maths'])
              
def search_by_roll_no(roll_no):
    students=read_data()
    for student in students:
        if student ["roll_no"]==roll_no:
            print("student found")
            print("Name:",student['name'])
            print("roll_no:",student['roll_no'])
            print("Marks:")
            print("Physics:",student['marks']['physics'])
            print("Chemistry:",student['marks']['chemistry'])
            print("Maths:",student['marks']['maths'])
            return
    print("student not found\n")
            
def main():
    while True:
        print("Menu:\n")
        print("1. add_students()\n")
        print("2. display all students:\n")
        print("3. Search by roll no:\n")
        print("4. Exit\n")
        choice=input("Enter your Choice:")
        if choice =='1':
            add_student()
        elif choice =='2':
            display_all_students()
        elif choice =='3':
            roll_no=input("enter roll_no to search:")
            search_by_roll_no(roll_no)
        elif choice =='4':
            print("Exit")
            break
        else:
            print("Invalid Choice\n")
            
if __name__=="__main__":
    main()          