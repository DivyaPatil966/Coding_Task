students = []
n=int(input("Enter number of students:"))
for i in range(n):
 name=input("Enter name:")
 roll_no=input("Eneter roll_no:")
 marks=input("marks:")
 physics=int(input("Eneter marks:"))
 chemistry=int(input("Enter marks:"))
 maths=int(input("Enetr marks:"))
 
 student={"name":name,"roll_no":roll_no,
          "marks":{"physics":physics,"chemistry":chemistry,"maths":maths}}
 
 students.append(student)
 print("\nstudent details:\n")
 
 for s in students:
     print("Name:",s["name"])
     print("roll_no:",s["roll_no"])
     print("Marks:")
     print("physics:",s["marks"]["physics"])
     print("chemistry:",s["marks"]["chemistry"])
     print("Maths:",s["marks"]["maths"])