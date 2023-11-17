
## 1. Describe the Problem
_Put or write the user story here. Add any clarifying notes you might have._
>as a user
>so that i can keep track of my tasks
 {{PROBLEM}} Function Design Recipe
>i want a program that i can add todo tasks to and see a list of them

>as a user
>so that i can focus on tasks to complete
>i want to mark tasks as complete and have them disappear from
## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
class TaskTracker():
    def add(self,task):
        #parameters:
        #   task: string, representing task
        pass
    def list_incomplete(self):
        #returns
        #list of incomplete tasks
        pass
    def mark_complete(self,index):
    #parameters
    # index: an integer representing the task to complete
    #side effect:
    #remove task at index from list of tasks
        pass
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""initially no tasks"""
tracker = TaskTrackers()
tracker.list_incomplete() # => []

"""when we add a task"""
tracker = TaskTrackers()
tracker.add("walk the dog")
tracker.list_incomplete() # => ["walk the dog"]

"""we add multiple tasks"""
tracker = TaskTrackers()
tracker.add("walk the dog")
tracker.add("walk the cat")
tracker.add("walk the fish")
tracker.list_incomplete() # => ["walk the dog", "walk the cat","walk the fish"]

"""we add mupltiple tasks and mark one complete disappears from list"""
tracker = TaskTrackers()
tracker.add("walk the dog")
tracker.add("walk the cat")
tracker.add("walk the fish")
tracker.mark_complete(1)
tracker.list_incomplete()
tracker.list_incomplete() # => ["walk the dog","walk the fish"]

"""we try to mark a track complete that does not exist (too low)""" 
tracker = TaskTrackers()
tracker.add("walk the dog")
tracker.mark_complete(-1) # raises an error "No such task to mark complete"
tracker.list_incomplete() # => ["walk the dog"]

"""we try to mark a track complete that does not exist (too high)""" 
tracker = TaskTrackers()
tracker.add("walk the dog")
tracker.mark_complete(2) # raises an error "No such task to mark complete"
tracker.list_incomplete() # => ["walk the dog"]
```
_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:
```python
# EXAMPLE


Ensure all test function names are unique, otherwise pytest will ignore them!

