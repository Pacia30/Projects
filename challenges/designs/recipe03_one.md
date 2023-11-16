 {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem
_Put or write the user story here. Add any clarifying notes you might have._

>as a user
>so i can manage my time
>i want to see an estimate of reading time for a test, assume i can read 200 words a
## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def estimate_reading_time(text):
    words = text.split()
    length = len(words)
    estimate_read_time = length/200
pass
    """
    Parameters:
        text: string containing words
        words: full "text" split into individual words so it is possible to count amount of words in text

    Returns: a string that states the estimated time
    """
## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

    estimate_read_time("my name is ippo") => "The estimate reading time for this text is 0.02 minutes"
#text article of labradors
    estimate_read_time("he Labrador Retriever was bred to be both a friendly companion and a useful working dog breed. Historically, they earned their keep as fishermen’s helpers: hauling nets, fetching ropes, and retrieving fish from the chilly North Atlantic. Today’s Labrador Retriever is as good-natured and hardworking as their ancestors, and they’re also America’s most popular breed. Modern Labs work as retrievers for hunters, assistance dogs, show competitors, and search and rescue dogs, among other canine jobs. When considering a Lab, we recommend adopting from rescue organizations or shelters to provide a loving home to a dog in need. However, if you decide to buy, it’s crucial to choose a reputable breeder. Conduct thorough research to ensure that the breeder follows ethical practices and values the well-being of their dogs. Reputable breeders prioritize the health and temperament of their Labrador Retriever puppies, conduct necessary health screenings, and provide a nurturing environment for the puppies. This active approach ensures that you bring home a healthy and happy pup while discouraging unethical breeding practices.") => "the estimate reading time for this text is 5.63 minutes"
_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

from lib.estimate_reading_time import *

def test_reading_time_ippo():
    assert estimate_read_time("my name is ippo") == "the estimate reading time for this text is 0.02 minutes"

def test_reading_time_labrador():
    assert estimade_read_time("The Labrador Retriever was bred to be both a friendly companion and a useful working dog breed. Historically, they earned their keep as fishermen’s helpers: hauling nets, fetching ropes, and retrieving fish from the chilly North Atlantic. Today’s Labrador Retriever is as good-natured and hardworking as their ancestors, and they’re also America’s most popular breed. Modern Labs work as retrievers for hunters, assistance dogs, show competitors, and search and rescue dogs, among other canine jobs. When considering a Lab, we recommend adopting from rescue organizations or shelters to provide a loving home to a dog in need. However, if you decide to buy, it’s crucial to choose a reputable breeder. Conduct thorough research to ensure that the breeder follows ethical practices and values the well-being of their dogs. Reputable breeders prioritize the health and temperament of their Labrador Retriever puppies, conduct necessary health screenings, and provide a nurturing environment for the puppies. This active approach ensures that you bring home a healthy and happy pup while discouraging unethical breeding practices.") == "the estimate reading time for this text is 0.85 minutes"


Ensure all test function names are unique, otherwise pytest will ignore them!

