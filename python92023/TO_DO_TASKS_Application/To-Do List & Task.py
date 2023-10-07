import json


class Task:
    def __init__(self,title,description):
        self.title=title
        self.description=description
        self.completed=False

def display_menu():
    print("====To-Do List Menu====")
    print("1. Add a Task ")
    print("2. View All saved Tasks ")
    print("3. Mark Task  as a complete  ")
    print("4. Delete tasks ")
    print("5. Edit tasks ")
    print("6. Save and Exit ")

tasks=[]
    
def add_task():
    title=input("Enter task title : ")
    description=input("Enter task description : ")
    new_task=Task(title,description)
    tasks.append(new_task)
    print("Task added! ")
           
def view_tasks():
    if not tasks:
        print("No Tasks Found! ")
    else:
        for index,task in enumerate(tasks,start=1):
            status="Completed" if task.completed else "Incompleted"
            print(f"{index}.{task.title}-{task.description}-{status}")
def mark_task_complete():
  view_tasks()
  task_index=int(input("Enter  the task number you want mark as completed.."))-1
  if 0<=task_index<len(tasks):
      tasks[task_index].completed=True
      print("Task marked as completed ")
  else:
      print("Invalid Task number!")

def save_task():
    with open("tasks.json","w") as file:
        task_list=[]
        for task in tasks:
            task_list.append({
                "title":task.title,
                "description":task.description,
                "completed":task.completed
            })
        json.dump(task_list,file)
        print("Task saved to tasks.json.")
def delete_tasks():
    view_tasks()
    task_index=int(input("Enter the task number you want to delete task! "))-1
    if 0<=task_index<len(tasks):
        del tasks[task_index]
        print("Task successfuly deleted")
    else:
        print("Invalid task number!")
def edit_tasks():
    view_tasks()
    task_index=int(input("Enter the task number you want to adit :"))-1
    if 0<=task_index<len(tasks):
        new_title=input("Enter new task title: ")
        new_description=input("Enter new task description: ")
        tasks[task_index].title=new_title
        tasks[task_index].description=new_description
        print("Task edited!.")
    else:
        print("Invalid Task number...")
def load_tasks():
    try:
        with open("tasks.json","r") as file:
            task_list=json.load(file)
            for task_data in task_list :
                task=Task(task_data["title"],task_data["description"])
                task.completed=task_data["completed"]
                tasks.append(task)
            print("Tasks loaded from tasks.json.")
            
    except FileNotFoundError:
        print("No task file found!. Starting with empty list.")
    
    
      
        
def main():
    while True:
        load_tasks()
        display_menu()
        choice=input("Enter your choice: ")
        if choice=="1":
            add_task()
        elif choice=="2":
            view_tasks()
        elif choice=="3":
            mark_task_complete()
        elif choice=="4":
            delete_tasks()
        elif choice=="5":
           edit_tasks()
        elif choice=="6":
            save_task()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option: ")
            
if __name__=="__main__":
    main()
    