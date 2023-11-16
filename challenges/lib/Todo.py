def todo_list(text):
    if "#TODO" in (text):
        return "The task is to be done!"
    elif (text) == "":
        return "A task has not been given, please give a task."
    else:
        return "The task is not to be done!"
    