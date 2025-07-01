#Task 1
student_dictionary = { 'Alice' : 85 ,'Ben' : 99 ,'Crade' : 0 }
x=input("Enter the student's name : ")
if (x in student_dictionary):
    print(f"{x}'s marks:{student_dictionary[x]}")
else:
    print("Student not foound")

#Task 2 
numbers = list(range(1, 11))
Extracted_list = numbers[:5]
reversed_first_five = Extracted_list[::-1]
print ("Original list",numbers)
print("Extracted list:", Extracted_list)
print("Reversed Extracted list:", reversed_first_five)
