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

class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    
    def average(self):
        if self.marks:
            return sum(int(mark) for mark in self.marks.values()) / len(self.marks)
    
students=[]
def add_student():
    students = read_data()    
    roll_no = [student["roll_no"] for student in students]
    while True:
        roll_number = input("Enter roll_no:")    

        if roll_number in roll_no:
            print("Student with this roll number already exists.")
        else:
            break
    name = input("Enter name:\n")
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
    students_data=read_data()
    if not students_data:
        print("No student to display")
        return
    print("\n All students")
    for s in students_data:
        student = Student(s['name'], s['roll_no'], s['marks']) 
        print("Name:",student.name)
        print("roll_no:",student.roll_no)
        print("Marks:")
        print("Physics:",student.marks['physics'])
        print("Chemistry:",student.marks['chemistry'])
        print("Maths:",student.marks['maths'])
        print("average Marks:",student.average()) 
               
def search_by_rollno(roll_no):
    students_data=read_data()
    for s in students_data:
        if s['roll_no'] == roll_no:
            student = Student(s['name'], s['roll_no'], s['marks']) 
            print("student found")
            print("Name:",student.name)
            print("roll_no:",student.roll_no)
            print("Marks:")
            print("Physics:",student.marks['physics'])
            print("Chemistry:",student.marks['chemistry'])
            print("Maths:",student.marks['maths'])
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
            search_by_rollno(roll_no)
        elif choice =='4':
            print("Exit")
            break
        else:
            print("Invalid Choice\n")
            
if __name__=="__main__":
    main()          
    


          
          



    
        