#question 1
list = [1,2,3,4,5,6,7,8,9]
even_list = []
print("The even numbers of the list are : ")
for i in range(len(list)):
    if list[i] % 2 == 0:
        even_list.append(list[i])
print(even_list)
print()
#question 2
list1 = [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]

merged_list = []
for i in range(len(list1)):
    if list1[i] % 2 == 1:
        merged_list.append(list1[i])

for i in range(len(list2)):
    if list2[i] % 2 != 1:
        merged_list.append(list2[i])

print("merged_list = ",merged_list)
print()
#question 3
list = [10, 20, 23, 11, 17]
list.sort()
print("The second largest element in the list is : ",list[-2])
