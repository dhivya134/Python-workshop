contact = {}
def add_contact():
    name = input("Enter the name of the contact to be added : ")
    number = input("Enter the contact number : ")
    contact[name] = number
    print("Contact added !")
def delete_contact():
    name =  input("Enter the name of the contact to be deleted : ")
    if name in contact:
        del contact[name]
        print("Contact deleted ! ")
    else:
        print("No such contacts")
def edit_contact():
    name =  input("Enter the name of the contact to edit : ")
    if name in contact:
        number = input("Enter the new contact number : ")
        contact[name] = number
        print("Contact edited ! ")
    else:
        print("No such contacts")
def search_contact():
    name =  input("Enter the name of the contact to be searched : ")
    if name in contact:
        print("Contact number of seached name is  ",contact[name])
    else:
        print("No such contacts")
def view_contact():
    print("contacts : ",contact)
actions = { 1:add_contact,2:delete_contact,3:edit_contact,4:search_contact,5:view_contact}
print("Contact Book \n press \n 1 to add a contact\n 2 to delete a contact\n 3 to edit a contact\n 4 to search a contact \n 5 to view contact \n 0 to exit")
while True:
    choice = int(input("Enter your choice : "))
    if choice in actions:
        action = actions[choice]
        action()  
    elif choice == 0:
        break
    else:
        print("Invalid Input")
    
    
