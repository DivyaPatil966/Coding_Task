import json

# to handle  all the data from rest file , use a global dict that has roll number as the key and Student Obj as the value.

def read_data():
    # read the rest data and create Student object
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
        
    # method to converter Student object to dict
    # method to display student object 
    
    
    def average(self):
        if self.marks:
            return sum(int(mark) for mark in self.marks.values()) / len(self.marks)
    
students=[]
def add_student():
    students = read_data()    # should not read rest data for every addition
    roll_no = [student["roll_no"] for student in students] # need not create this for every addition
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
    students.append({ # this should be an object
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
    students_data=read_data() # better do it at start of the program
    if not students_data:
        print("No student to display")
        return
    print("\n All students")
    for s in students_data:
        student = Student(s['name'], s['roll_no'], s['marks']) # should not create Student obj every time
        print("Name:",student.name)
        print("roll_no:",student.roll_no)
        print("Marks:")
        print("Physics:",student.marks['physics'])
        print("Chemistry:",student.marks['chemistry'])
        print("Maths:",student.marks['maths'])
        print("average Marks:",student.average()) 
               
def search_by_rollno(roll_no):
    # get student by O(1)
    students_data=read_data() # dont read from rest data every time 
    student_by_rollno={student['roll_no']:student for student in students_data} # u r looping through all the students so time taken is n
    student_data=student_by_rollno.get(roll_no)
    if student_data:    
        student = Student(student_data['name'], student_data['roll_no'], student_data['marks']) 
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
    


          
          



    
        