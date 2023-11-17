import pytest
from lib.tasktracker   import*

"""not given task"""
def test_initially_has_no_tasks():
    tracker = TaskTracker()
    assert tracker.list_incomplete() == []
#
#
#"""when we add a task"""
def test_add_task_reflectected_in_tasks():
    tracker = TaskTracker()
    tracker.add("walk the dog")
    assert tracker.list_incomplete() == ["walk the dog"]
#
#"""we add multiple tasks"""
def test_add_mutitple_tasks():
    tracker = TaskTracker()
    tracker.add("walk the dog")
    tracker.add("walk the cat")
    tracker.add("walk the fish")
    assert tracker.list_incomplete()  == ["walk the dog", "walk the cat","walk the fish"]
#
#"""we add mupltiple tasks and mark one complete disappears from list"""
def test_marks_tasks_complete():
    tracker = TaskTracker()
    tracker.add("walk the dog")
    tracker.add("walk the cat")
    tracker.add("walk the fish")
    tracker.mark_complete(1)
    assert tracker.list_incomplete()  == ["walk the dog","walk the fish"]
#
#"""we try to mark a track complete that does not exist (too low)""" 
def test_mark_task_complete_too_low():
    tracker = TaskTracker()
    tracker.add("walk the dog")
    with pytest.raises(Exception) as e:
        tracker.mark_complete(-1) 
    assert str(e.value) == "No such task to mark complete"
    assert tracker.list_incomplete() == ["walk the dog"]

#"""we try to mark a track complete that does not exist (too high)""" 
def test_mark_task_complete_too_high():
    tracker = TaskTracker()
    tracker.add("walk the dog")
    with pytest.raises(Exception) as e:
        tracker.mark_complete(1) 
    assert str(e.value) == "No such task to mark complete"
    assert tracker.list_incomplete() == ["walk the dog"]
