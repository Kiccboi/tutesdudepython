#Task1 
def factorial(n):
    if n<2:
        return 1 
    else:
        return n * (factorial(n-1))
    
n=int(input("Enter a number: "))
x=factorial(n)
print(f"Factorial of {n} is : {x}")

#Task 2
import math 
x=int(input("Enter a number :"))
print("Square root : ",math.sqrt(x))
print("Logarithm : ",math.log(x))
print("Sine: ",math.sin(x))
