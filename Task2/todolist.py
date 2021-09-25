def add_task():
    task = input("Enter the new task : ")
    priority = int(input("please enter the priority (1,2,3) : "))
    todolist.append([task,priority])
    print(todolist)

def edit_task():
    old_task= input("Enter the task to change : ")
    new_task= input("Enter the new task : ")
    priority = int(input("please enter the priority (1,2,3) : "))
    for subarray in todolist:
        for old_task in subarray:
            indexno = todolist.index(subarray)
    todolist[indexno] = [new_task,priority]
def delete_task():
    task = input("Enter the task to be deleted : ")
    for subarray in todolist:
        if task in subarray:
            indexno = todolist.index(subarray)
            todolist.pop(indexno)
    print(todolist)
    


todolist = []
actions = { 1:add_task,2:edit_task,3:delete_task}
print("Todolist App \n press \n 1 to add a new task\n 2 to edit a new task\n 3 to delete task\n 4 to View tasks based on priority \n 0 to exit")
while True:
    choice = int(input("Enter your choice : "))
    if choice in actions:
        action = actions[choice]
        action()
    elif choice == 4:
        todolist.sort(key=lambda x:x[1])
        for subarray in todolist:
            print(subarray[0])
        
    
    elif choice == 0:
        break
