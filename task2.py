import json

def read_data():
    with open ("students.json") as file:
        students=json.load(file)
        return students
        
def write_data(students):
    with open("students.json","w") as file:
        json.dump(students,file,indent=4)
       
        
def add_student():
    students_details=read_data()
    name=input("Enter name:\n")
    roll_no=input("Enter roll_no:")
    physics=int(input("Enter Physics marks:"))
    chemistry=int(input("Enter chemistry marks:"))
    maths=int(input("Enter maths marks"))
    marks={"physics":physics,"chemistry":chemistry,"maths":maths}
    students_details.append({"name":name,"roll_no":roll_no,"marks":marks})
    print("student added")
    write_data(students_details)
    
    
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
        print("Enter your choice:\n")
        print("1. add_students()\n")
        print("2. display all students:\n")
        print("3. Search by roll no:\n")
        print("4. Exit\n")
        choice=input("Choice:")
        if choice =='1':
            add_student()
            
        elif choice=='2':
            display_all_students()
        elif choice=='3':
            roll_no=input("enter roll_no to search:")
            search_by_roll_no(roll_no)
        elif choice=='4':
            print("Exit")
            break
        else:
            print("Invalid Choice\n")
            
if __name__=="__main__":
    main()          