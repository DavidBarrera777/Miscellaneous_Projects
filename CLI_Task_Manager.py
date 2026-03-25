import json

#json file located in the same directory as the py file 
file = 'task.json'


#This function holds the task list json file
#If the file is not found, it returns an empty list 
def task_list():
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except IOError as e:
        print(f'Error handling file {file}: {e}')
        return []



#This function is used to view the tasks and determine wheter the tasks are done or not
#by wheter or not the key of done is equal to True or False
#This function aslo prints the task to the user
def view_tasks():
    try:
        with open(file, 'r') as f:
            tasks = json.load(f)
            for i in tasks:
                if i['done'] == False:
                    print(f'[✖] {i['task'].capitalize()}')
                else:
                    print(f'[✓] {i['task'].capitalize()}')
    except IOError as e:
        print(f'Error handling file {file}: {e}')
    return 


#This function adds taks to the json file by first ask the user what task they would like to add
#then it is appended to the json file list as a task and the key done is set to false to represent 
#the task has yet to be completed
def add_task(taskList):
    user_input = input("Enter a task you would like to enter: ")
    taskList.append({'task':user_input, 'done':False})
    try:
        with open(file, 'w') as f:
            json.dump(taskList, f,indent=4)
    except IOError as e:
        print(f'Error handling file {file}: {e}')
    return 


#The function displays the list in numerical order then asks the user which task they would like
#to complete, the response is taken as an int
#Depending on the user input, the key of that specific task will be set to True
def complete_task(taskList):
    for i, task in enumerate(taskList):
        print(f'{i+1}. {task['task']}')
    try:
        index = int(input('Which task is complete? '))-1
        taskList[index]['done'] = True
        with open(file, 'w') as f:
            json.dump(taskList, f, indent=4)
        print('Task marked as complete')
    except IOError as e:
        print(f'Error handling file {file}: {e}')
        
    return 


#This function is responsible for deleting task from the task list by asking the user which task
#they would like to delete and poping it from the list and updating the json file accordingly
def delete_task(taskList):
    print("Here are your most recent task:")
    for i, task in enumerate(taskList):
        print(f'{i+1}. {task['task']}')
    user_input = int(input('Which task would you like to delete? '))-1
    taskList.pop(user_input)

    try:
        with open(file, 'w') as f:
            json.dump(taskList, f,indent=4)
            print('List updated successfully')
    except IOError as e:
        print(f'Error handling file {file}: {e}')

    return 




#This the main function that is responsivble for all the main menu logic
#The whole program runs within a while loop and displays and asks the user which 
#task they would like to complete
def main():
    print('Welcome to CLI Task Manager')
    print('1. View Tasks')
    print('2. Add Tasks')
    print('3. Complete Tasks')
    print('4. Delete Tasks')
    print('5. Exit')
    taskList = task_list()

    while True:
        selection = int(input('Enter a number for the task you would like to complete: '))
        if selection == 1:
            view_tasks()
        elif selection == 2:
            add_task(taskList)
        elif selection == 3:
            complete_task(taskList)
        elif selection == 4:
            delete_task(taskList)
        elif selection == 5:
            print('Program ended succsefully')
            break

    return


if __name__ == '__main__':
    main()

