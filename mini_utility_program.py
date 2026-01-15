print("1. Factorial")
print("2. USD to INR")
print("3. Length of list")
print("4. Print list")
print("5. Exit")

choice = int(input("Enter your choice: "))

def factorial(n): #factorial program
    fact=1
    for i in range(1,n+1):
        fact *=i
    return fact

def usd_to_inr(USD): #USD_TO_INR program
    a=USD*90
    return a
 
l=[23,35,78,24,24,89,35] # length of a list
l1=["nina","jay","priya","nivi","hari","puja"]
def list_length(lst):
    a=len(lst)
    return a

l2=[68,24,56,25,63,63,43,536,78] # print list element in a single line
def element(lst):
    for item in lst:
        print(item,end=" ")

if(choice==1):
    n=int(input("enter a number:"))
    print(factorial(n))
elif(choice==2):
    USD=int(input("enter a USD:"))
    print(usd_to_inr(USD))
elif(choice==3):
    print(list_length(l))
    print(list_length(l1))
elif(choice==4):
    element(l2)
elif(choice == 5):
    print("Exiting program")






