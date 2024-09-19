todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")


def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' removed from the list.")
    else:
        print(f"Task '{task}' not found in the list.")


def show_tasks():
    if todo_list:
        print("Your To-Do List:")
        for index, task in enumerate(todo_list, 1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty!")


add_task("Learn Power bi")
add_task("Complete Python project")
add_task("Go to the gym")
add_task("Draft an email")

show_tasks()


remove_task("Draft an email")


show_tasks()
