import unittest

from linked_list.linked_list_zipped import LinkedList

class TestlinkedList(unittest.TestCase):
 
    def test_linked_list_zip_happy_path(self):
            """
            This is the happy path test
            
            """
            ll1= LinkedList()
            ll1.insert(1)
            ll1.insert(3)
            ll1.insert(5)
            ll2= LinkedList()
            ll2.insert(2)
            ll2.insert(4)
            ll2.insert(6)
            ll=LinkedList()
            
            # self.assertEqual(ll.linked_list_zip(ll1,ll2).__str__(), "head -> { 5 } -> { 6 } -> { 3 } -> { 4 } -> { 1 } -> { 2 } -> NULL")


    # def test_linked_list_edge_case():
    #     "This test checks if one of the lists is empty"
    #     ll1= LinkedList()
    #     ll1.insert(1)
    #     ll1.insert(3)
    #     ll1.insert(5)
    #     ll2= LinkedList()
    #     ll=LinkedList()
    #     self.assertEqual(ll.linked_list_zip(ll1,ll2).__str__(), ll1.__str__())



    def test_zip_lists_expected_failure(self):
        ll1= LinkedList()
        ll2= LinkedList()
        ll=LinkedList()
        with self.assertRaises(Exception):
            ll.zip_lists(ll1,ll2)



            
    # def test_merge_list_list1_longer():
    #     list1 = LinkedList()
    #     list2 = LinkedList()
    #     list1.insert("3")
    #     list1.insert("1")
    #     list1.insert("4")
    #     list2.insert("9")
    #     list2.insert("5")
    #     actual = str(linked_list_zip(list1, list2))
    #     expected = "{ 4 } -> { 5 } -> { 1 } -> { 9 } -> { 3 } -> NULL"
    #     assert actual == expected


    # @pytest.fixture
    # def ll_list():
    #     """
    #     Sets up a linked list instance along with adds a few nodes for testing
        
    #     """
    #     ll = LinkedList()
    #     ll.insert("a")
    #     ll.insert("b")
    #     ll.insert("c")
    #     return ll

        