
class Node:
    """
     Class for the Node instances
     """
    
    def __init__(self, value):
        self.value = value
        self.next = None


if __name__ == "__main__":
    pass


class LinkedList:
    """
    Class for the LinkedList instances
    Upon instantiation, an empty Linked List should be created.
    """

    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head is None:
            self.head = node

        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def insert(self, value):
        """
        method to add a new node with that value to the head of the list with an O(1) Time performance.
        """
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def includes(self, value):
        """
        method to check if the given value in the liked list
        """
        current = self.head
        while current:
            if current.value == value:
                return True
            else:
                current = current.next
        return False

    def __str__(self):
        """
        method that returns a string that represents all list elements
         formatted as:
           "{ a } -> { b } -> { c } -> NULL"
        """
        elements = "head -> "
        if self.head is None:
            elements += "NULL"
        else:
            current = self.head
            while current:
                elements += "{ " + f"{current.value}" + " } -> "
                current = current.next
            elements += "NULL"
            print (elements)
            return elements
    
 
    def append(self, value):
        """method to append new node to the end of the list"""

        current = self.head
        while current:

            print(current.value)
            if current.next == None:
                current.next = Node(value)
                return self.__str__()
            else:
                current = current.next

        self.head = Node(value)
        return self.__str__()



    def insert_before(self, value, new_value):
        """method to insert new element before the given element of the list"""

        if self.includes(value):
            current = self.head
            previous = None
            while current:
                if current.value == value:
                    node = Node(new_value)
                    node.next = current
                    if previous:
                        previous.next = node
                    else:
                        self.head = node
                    return self.__str__()
                previous = current
                current = current.next
        else:
            return 'Value is not in the list'


    def insert_after(self, value, new_value):
        """method to insert new element after the given element of the list"""

        if self.includes(value):
            current = self.head
            while current:
                if current.value == value:
                    node = Node(new_value)
                    node.next = current.next
                    current.next = node
                    return self.__str__()
                current = current.next
        else:
            return 'Value is not in the list'



    def kth_from_end(self, k):
            """
            Return the node's value that is k places from the tail of the linked list.
            """
            temp = self.head
            length = 0
            if type(k)!= type(5) or k<0:
                print("the index should be a positive integer value")
                return "the index should be a positive integer value"
            while temp.next is not None:
                temp = temp.next
                length += 1
            if k > length:
                """
                if the entered number is bigger than the length of the linked list
                """
                print('Location is greater than the length of LinkedList')
                return 'Location is greater than the length of LinkedList'
            temp = self.head
            for i in range(0, length - k):
                temp = temp.next
            print(temp.value)
            return temp.value






if __name__=='__main__':
        ll=LinkedList()
        ll.insert('a')
        ll.insert('b')
        ll.insert(4)
        ll.insert('d')
        
        ll.__str__()

        ll.kth_from_end(2)

    



    

    

   

     
        



# def printLL(self):
#         "adds the values of the nodes in the linked list to an array"
#         current = self.head
#         data=[]
#         while(current):
#             data.append(current.data)
#             current = current.next
#         print(data)
#         return data



# def size(self):
#         """
#         returns the size of the linked list "how many node is in the list"
#         """
#         current = self.head
#         count = 0
#         while current:
#             count += 1
#             current = current.get_next()
#         print(count)
#         return count