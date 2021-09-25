# pattern 1
def plus_row():
    print("+",end=" ")
    for i in range(4):
        print("-",end=" ")
    print("+",end=" " )
    for i in range(4):
        print("-",end=" ")
    print("+")

def other_row():
    print("|",end=" ")
    for i in range(4):
        print(" ",end=" ")
    print("|",end=" " )
    for i in range(4):
        print(" ",end=" ")
    print("|")

for i in range(1,12):
    if i == 1 or i == 6 or i == 11:
        plus_row()
    else:
        other_row()
#pattern 2
def star_row(n):
    for i in range(n):
        print("*",end=" ")

n = int(input("Enter the number of rows : "))
for i in range(1,n+1):
    star_row(i)
    print()
#pattern 3
row = int(input("Enter the Number of rows"))
for i in range(row):
    for s in range(row, i, -1):
        print(end=" ")
    for j in range(i+1):
        print(end="* ")
    print()

    
    
