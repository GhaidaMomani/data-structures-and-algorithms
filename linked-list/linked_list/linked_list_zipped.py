    

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
    
    def append(self, node):
        if self.head is None:
            self.head = node

        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
    
    def linked_list_zip(ll1, ll2):
        ll1_current = ll1.head
        ll2_current = ll2.head

        """
        Optimal solution 
            - loop thorugh ll2
            - if the ll1 current is empty and the ll2 current is not empty:
                - append ll2 to ll1
            - insert after ll1.head 
            1 -> 2 -> 3
            4 ->5 ->6
        """
        while (ll1_current and ll2_current != Null):
            ll1_next = ll1_current.next
            ll2_next = ll2_current.next
            ll1_current.next = ll2_current
            ll1_current = ll1_next
            if ll1_current != Null:
                ll2_current.next = ll1_current
            
            ll2_current = ll2_next
        return ll1
        












        
    # def linked_list_zip(self, linkedlist_1, linkedlist_2):
    #         """
    #         zip list means merge two lists together, So this function will take two linked lists 
    #         as parameters 
    #         it is like making a braid or when you use the zipper in clothes to 
    #         close your jacket or something,You take list1 head and then add the list2  head
    #         and so on.. 
    #         and it will return one zipped list 
    #         """

    #         if linkedlist_1.head == None:
    #             return linkedlist_2
    #         elif linkedlist_2.head == None:
    #             return linkedlist_1

    #         if linkedlist_1.head ==None and linkedlist_2.head==None:
    #                 print("both lists Can't be empty")
    #                 raise Exception("both lists Can't be empty")

    #         new_ll = LinkedList()
    #         curr1 = linkedlist_1.head
    #         curr2 = linkedlist_2.head

    #         while curr1 or curr2:
    #             if curr1:
    #                 """
    #                 if the new list already has nodes in it
    #                 we make an extra check 
    #                 """

    #                 if new_ll.head == None:
    #                     new_ll.insert(curr1.value)
    #                 else:
    #                     new_ll.append(curr1.value)

    #             if curr2:
    #                 """
    #                 if the new list already has nodes in it
    #                 we make an extra check 
    #                 """
    #                 if new_ll.head == None:
    #                     new_ll.insert(curr2.value)
    #                 else:
    #                     new_ll.append(curr2.value)

    #             if curr1 and curr1.next:
    #                 curr1 = curr1.next
    #             else:
    #                 curr1 = False

    #             if curr2 and curr2.next:
    #                 curr2 = curr2.next
    #             else:
    #                 curr2 = False

    #         return new_ll
