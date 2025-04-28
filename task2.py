students=[]
def add_student():
    name=input("Enter name:\n")
    roll_no=input("Enter roll_no:")
    marks=input("Enter Marks:")
    students.append({"name":name,"roll_no":roll_no,"marks":marks})
    print("student added")
def display_all_students():
    if not students:
        print("No students to display")
        return
    print("\n All students")
    for student in students:
        print("Name:",student['name'],"roll_no:",student['roll_no'],"marks:",student['marks'])
              
def search_by_roll_no(roll_no):
    for student in students:
        if student ["roll_no"]==roll_no:
            print("student found")
            print("name:",student["name"],"Roll_no:",student["roll_no"],"marks:",student["marks"],"\n")
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