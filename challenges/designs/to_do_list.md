 {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._
> As a user
> So that i can keep track of my tasks
> I want to check if a text includes the string #TODO

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def todo_list()
#will need to check if "#todo" in text using if and in statements
#will be given a text 
if '#TODO' in (text):
    pass
#must be #TOTO
#text = string (eg walk the dog #todo, eg feed #TODO the cat)

#return if text is to do or not to do 

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
todo_list("walk the dog #TODO") => "The task is to be done!"
todo_list("feed the cat #todo") => "The task is not to be done!"
todo_list("walk the fish") => "The task is not to be done!"
todo_list("Go for a run #TODo") => "The task is not to be done!"
todo_list("") => "A task has not been given, please give a task."

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
from lib.todo import *
#when given the key word #TODO
def test_todo_list_walk_dog():
    assert todo_list("walk the dog #TODO") == "The task is to be done!"

#when given key word but lowercase
def test_todo_list_feed_cat():
    assert todo_list("feed the cat #todo") == "The task is not to be done!"

#when given task with no key word
def test_todo_list_walk_fish():
    assert todo_list("walk the fish") == "The task is not to be done!"

#when keyword given but one letter is lowercase
def test_todo_list_run():
    assert todo_list("Go for a run #TODo") == "The task is not to be done!"

#when given nothing
def test_todo_list_nothing():
    assert todo_list("") == "A task has not been given, please give a task."
```

Ensure all test function names are unique, otherwise pytest will ignore them!

