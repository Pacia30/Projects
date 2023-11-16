from lib.Todo import*

def test_todo_list_walk_dog():
    assert todo_list("walk the dog #TODO") == "The task is to be done!"

def test_todo_list_feed_cat():
    assert todo_list("feed the cat #todo") == "The task is not to be done!"

def test_todo_list_nothing():
    assert todo_list("") == "A task has not been given, please give a task."

def test_todo_list_run():
    assert todo_list("Go for a run #TODo") == "The task is not to be done!"

def test_todo_list_walk_fish():
    assert todo_list("walk the fish") == "The task is not to be done!"