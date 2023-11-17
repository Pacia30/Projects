 {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem
>As a user
> So that i can keep track of my music listening
>I want to add tracks I've listened to and see a list of them

_Put or write the user story here. Add any clarifying notes you might have._
## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
class MusicTracker():
    def add(self,music):
        #parameters: music: a string representing music
        #adds music to list
    def musiclist(self):
        #returns a list of music listened to
```
## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""
Start with empty list, nothing added
"""
def test_empty_list():
    musictracked = MusicTracker()
    add("") == []

"""
listened to one song. add song to list
"""
def test_listened_one_song():
    musictracked = MusicTracker()
    musictracked.add("Ippos song") 
    musictracked.musiclist() == ["Ippos song"]

"""
listened to multiple songs. add songs to list
"""
def test_listened_mutiple_songs():
    musictracked = MusicTracker()
    musictracked.add("Ippos song")
    musictracked.add("Echos sing song") 
    musictracked.add("Rengar sing song") 
    musictracked.musiclist() == ["Ippos song"]
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:
```python
# EXAMPLE


Ensure all test function names are unique, otherwise pytest will ignore them!

