#question 1
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
if a<b:
    print("The smallest number is : ",a)
else:
    print("The smallest number is : ",b)
print()
#question2
n= int(input("Enter the number : "))
if n%2==0:
    print(n,"is an even number")
else:
    print(n,"is an odd number")
print()
#question3
n= int(input("Enter the number : "))
if n>0:
    print(n,"is a positive number")
elif n<0 :
    print(n,"is a negative number")
else :
    print("The number is zero")
print()
#question4
mark = int(input("Enter the mark : "))
if mark > 90:
    print("O grade")
elif mark >= 81 and mark <= 90:
    print("A grade")
elif mark >= 71 and mark <= 80:
    print("B grade")
elif mark >= 61 and mark <= 70:
    print("C grade")
elif mark >= 51 and mark <= 60:
    print("D grade")
else :
    print("U grade")
print()
#question 5
p = int(input("Enter the amount : "))
t = int(input("Enter the time : "))
r = int(input("Enter the rate : "))
print("The simple interest SI is : ",(p*t*r)/100)
print()
#question 6
char = input("Enter the character: ")
if(char=='A' or char=='a' or char=='E' or char =='e' or char=='I'
 or char=='i' or char=='O' or char=='o' or char=='U' or char=='u'):
    print(char, "is a Vowel")
else:
    print(char, "is a Consonant")




list = [10, 20, 23, 11, 17]
list.sort()
print("The second largest element in the list is : ",list[-2])
