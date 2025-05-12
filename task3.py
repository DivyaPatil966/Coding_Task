class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    
    def average(self):
        if self.marks:
            return sum(self.marks.values())/len(self.marks)
    
students=[]
def add_student():
    name=input("enter the name:")
    roll_no=input("Enetr the roll_no:")
    physics=int(input("enter the MArks:"))
    chemistry=int(input("Enter the marks:"))
    maths=int(input("Enter the marks:"))
    marks={
        "physics":physics,
        "chemistry":chemistry,
        "maths":maths
    }
    student=Student(name,roll_no,marks)
    students.append(student)
    print("student added successfully")

def display_all_students():
    if not students:
        print("No student to display")
        return
    print("\n All students")
    for student in students:
        print("Name:",student.name)
        print("roll_no:",student.roll_no)
        print("Marks:")
        print("Physics:",student.marks['physics'])
        print("Chemistry:",student.marks['chemistry'])
        print("Maths:",student.marks['maths'])
        print("average Marks:",student.average()) 
               
def search_by_rollno(roll_no):
    for student in students:
        if student.roll_no==roll_no:
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
    


          
          



    
        