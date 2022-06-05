
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




    # def insert(self, data):
    #         "inserts a new node to the linked list as the head of the list"
    #         newNode = Node(data)
    #         if(self.head):
    #             current = self.head
    #             while(current.next):
    #                 current = current.next
    #             current.next = newNode
    #         else:
    #             self.head = newNode

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



    def linked_list_zip(self, linkedlist_1, linkedlist_2):
        """
        zip list means merge two lists together, So this function will take two linked lists 
        as parameters 
        it is like making a braid or when you use the zipper in clothes to 
        close your jacket or something,You take list1 head and then add the list2  head
        and so on.. 
        and it will return one zipped list 
        """

        if linkedlist_1.head == None:
            return linkedlist_2
        elif linkedlist_2.head == None:
            return linkedlist_1

        if linkedlist_1.head ==None and linkedlist_2.head==None:
                print("both lists Can't be empty")
                raise Exception("both lists Can't be empty")

        new_ll = LinkedList()
        curr1 = linkedlist_1.head
        curr2 = linkedlist_2.head

        while curr1 or curr2:
            if curr1:
                """
                if the new list already has nodes in it
                we make an extra check 
                """

                if new_ll.head == None:
                    new_ll.insert(curr1.value)
                else:
                    new_ll.append(curr1.value)

            if curr2:
                """
                if the new list already has nodes in it
                we make an extra check 
                """
                if new_ll.head == None:
                  new_ll.insert(curr2.value)
                else:
                    new_ll.append(curr2.value)

            if curr1 and curr1.next:
                curr1 = curr1.next
            else:
                curr1 = False

            if curr2 and curr2.next:
                curr2 = curr2.next
            else:
                curr2 = False

        return new_ll


    # def __str2__(self):
    #     """
    #     returns a string for each node in the list and which node is it pointing at 
    #     """
    #     output = ""
    #     if self.head is None:
    #         output = "Empty linked list"
    #         print(output)
    #     else:
    #         current = self.head
    #         while(current):
    #             output+= f'{current.value} --> '
    #             current = current.next
            
    #         output+= "None"
    #     print(output)
    #     return output


if __name__=='__main__':
        # ll=LinkedList()
        # ll.insert('a')
        # ll.insert('b')
        # ll2=LinkedList()
        # ll2.insert('cc')
        # ll2.insert('dd')
        # ll_3=LinkedList()
        # ll_3.linked_list_zip(ll,ll2)
        
        # ll.__str__()

        # ll.kth_from_end(2)

            ll1= LinkedList()
            ll1.insert(1)
            ll1.insert(3)
            ll1.insert(5)
            ll2= LinkedList()
            ll2.insert(2)
            ll2.insert(4)
            ll2.insert(6)
            ll2.insert(8)
            ll2.insert(10)
            ll=LinkedList()
            ll.linked_list_zip(ll1, ll2)

            ll.__str__()



    

    

   

     
        



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