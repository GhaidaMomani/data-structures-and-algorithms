
# Data Structures and Algorithms

## Code 401 - Advanced Software Development




By [Ghaida Al Momani] (https://github.com/GhaidaMomani).

>>>>>Welcome to Code 401.
<br/>
<hr/>
<br/>



# Stacks and Queue:FIFO Animal Shelter
Method that will manipulate data in stacks and queues.

## [PR](https://github.com/GhaidaMomani/data-structures-and-algorithms/pull/10)

# Challenge
Without using any builtin functionality, manipulate stack and queue data. Add a new Node Add / Remove to / from a stack Add / Remove to / from a queue Exception error handling

PseudoQueue Using 2 Stacks invoke queue

Fifo_Anmial_Shelter Using First in First Out add and remove cats and dogs.

Multi Bracket Validation

# Approach & Efficiency
* enqueue(animal) method time big O(1), space big O(1)
* dequeue(pref) method time big O(n), space big O(n)


# Whiteboard
![](../../assets/animal%20shelter.jpg)




# API
[Code](../fifo-animal-shelter/fifo_animal_shelter/fifo_animal_shelter.py)




# Solution

```python
  def dequeue(self, pref):
        """
        Method to take only preferable type of animal from the shelter using the  FIFO approach
        """
        adopted_animal = None

        while not self.queue1.is_empty():
            if self.queue1.front.type == pref.lower() and adopted_animal == None:
                adopted_animal= self.queue1.dequeue()
            else:
                self.queue2.enqueue(self.queue1.dequeue())

        while not self.queue2.is_empty():
            self.queue1.enqueue(self.queue2.dequeue())

        return adopted_animal




```




<hr/>
 <br/><br/>

<p align="right">Ghaida Al Momani, Software Engineer</p>
<p align="right">Jordan, Amman</p>

<p align="right">22, 30 MAR </p>