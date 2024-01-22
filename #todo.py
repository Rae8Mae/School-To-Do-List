#todo
#add item
#add input?
#Initialize
todolist= []

def add():
    item = input("what item do you want to add? ")
    todolist.append(item)

def remove():
    item = input("what item do you want to remove? ")
    todolist.remove(item)

def complete():
    item = input("what item do you want to mark as done? ")

    i = todolist.index(item) 
    todolist[i] = "✓"

def view():
    print(todolist)

def removeall():
    todolist.clear()

def alpha():
    sort_list = sorted(todolist)
    print(sort_list)

def number():
    size= len(todolist)
    print(size)

while True:
    print("select option \n1. add item \n2. remove item \n3. complete item \n4. view list \n5. exit program \n6. remove all tasks \n7. Sort list alphabetically \n8. print number of items")
    option = int(input("option:"))
    if (option == 1):
        add()

    if (option == 2):
        remove()

    if (option == 3):
        complete()

    if (option == 4):
        view()
    if(option == 6):
        removeall()
    if(option == 7):
        alpha()
    if(option == 8):
        number()
    if (option == 5):
        quit()
        break


#main
