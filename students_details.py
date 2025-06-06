import json
students={}
# to handle  all the data from rest file , use a global dict that has roll number as the key and Student Obj as the value.

def read_data():
    # read the rest data and create Student object
    global students
    try:
        with open ("students.json") as file:
            students=json.load(file)
            students = {student['roll_no']:Student.from_dict(student) for student in students}
    except FileNotFoundError:
        students = {}
    except json.JSONDecodeError:
        students = {}
          
def write_data(students):
    with open("students.json","w") as file:
        json.dump([student.to_dict() for student in students.values()],file,indent=4)      #comprehension

class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
        
    # method to converter Student object to dict
    # method to display student object 
    
    
    def average(self):
        if self.marks:
            return sum(int(mark) for mark in self.marks.values()) / len(self.marks)
        
    def display(self):
        print("Name: {}".format(self.name))
        print("Roll No: {}".format(self.roll_no))
        print("Marks:")
        for subject, mark in self.marks.items():
            print("  {}: {}".format(subject.capitalize(), mark))
        print("Average: {:.2f}\n".format(self.average()))
        
        
    def to_dict(self):
        return {'name':self.name,
        'roll_no':self.roll_no,
        'marks':self.marks
        }
    @classmethod
    def from_dict(cls,data):
        return cls(data['name'],data['roll_no'],data['marks'])
        

def add_student():
     # need not create this for every addition
    while True:
        roll_number = input("Enter roll_no:")    

        if roll_number in students:
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
    marks={'physics':physics,
           'chemistry':chemistry,
           'maths':maths}
    student=Student(name,roll_number,marks)
    students[roll_number]=student
    write_data(students)
    print("students added successfully")

def display_all_students(): 
    
    if not students:
        print("No student to display")
        return
    print("\n All students")
    for s in students.values():
        s.display()
               
def search_by_rollno(roll_no):
    s = students.get(roll_no)
    if s:     
        print("student found")
        s.display()
    else:
        print("student not found\n")

def main():
    read_data()
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