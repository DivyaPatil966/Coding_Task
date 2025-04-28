for i in range(5,11):
    print(i,end=" ")
print("\n")
for i in range(11,5,-1):
    print(i,end=" ")
print("\n")
string1="python"
string2=" python programming"
print("concatenation=",string1+string2)
print("repitation=",string1*2)
print("repetation=",string2*3)


list=[]
print("Blank List=",list)
list=["python","programming"]
print(list)
print(list[1])
print(list[0])

dict=dict()
print("empty dictionary")
dict1={
    "name":"Divya",
    "Roll_no":326,
    "Marks":45
}
print("student details=",dict1)
print("1st dict:",dict1["name"])
print("2nd dict:",dict1["Roll_no"])
print("3rd dict:",dict1["Marks"])