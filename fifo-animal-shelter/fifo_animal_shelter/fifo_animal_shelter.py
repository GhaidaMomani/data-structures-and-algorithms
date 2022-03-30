import copy

class Node:
    """ 
    This class is  for createing Node instances
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    """
   This class implements the queue data structure methods 
    """

    def __init__(self):
    
        self.front = None
        self.rear = None

    def is_empty(self):
        """
          check if Queue is empty
        """

        if self.front == None:
            return True
        return False


    def enqueue(self, new_node):
        """
        Method that takes any value as an argument and adds a new node with that value to the back of the queue

         """

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """
        Method that removes the node from the front of the queue, and returns the node’s value.
        """

        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp
        else:
            return None

    def peek(self):
        """
        Method that returns the value of the node located in the front of the queue, without removing it from the queue.
        """

        if not self.is_empty():
            return self.front.value
        return None

class Animal:
    """
    This class creates animal instances so the other types of animals inherit from it 
    """
    def __init__(self, pet_name):
        self.value = pet_name
        self.next = None

class Cat(Animal):
    """
   This class creates Cat instances and inherits it's properties from Animal class
   cat is a sub type of an animal 
    """
    type = 'cat'

class Dog(Animal):
    """
    This class creates dog instances and inherits it's properties from Animal class
    gog is a sub type of an animal 
    
    """
    type = 'dog'


class AnimalShelter:
    """
    This class  which holds only dogs and cats instances.
    It  operates using a first-in, first-out approach.
    """
    def __init__(self):
        """
        Method to initiate Animal shelter instance with creating two empty Queues
        """
        self.queue1 = Queue()
        self.queue2 = Queue()

    def enqueue(self, animal):
        """
        Method to add animal to the shelter usinf FIFO approach
        """
        if isinstance(animal, Cat) or isinstance(animal, Dog):
            self.queue1.enqueue(animal)
        else:
            return "Animal must be cat or dog"

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









