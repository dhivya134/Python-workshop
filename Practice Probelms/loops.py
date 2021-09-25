#question 1
n = int(input("Enter the number : "))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print("The sum is : ",sum)
print()
#question 2
n1 = int(input("Enter the starting number : "))
n2 = int(input("Enter the ending number : "))
sum = 0
for i in range(n1,n2+1):
    sum = sum + i
print("The sum is : ",sum)
print()
#question 3
n = int(input("Enter the  number : "))

factorial = 1
for i in range(1,n+1):
    factorial = factorial * i
print("The factorial of ",n ," is : ",factorial)
print()
#question 4
n1 = int(input("Enter the starting number : "))
n2 = int(input("Enter the ending number : "))
print("The odd numbers between ",n1,"and",n2,"are : ")
for i in range(n1,n2+1):
    if i%2 == 1:
        print(i)
print()


