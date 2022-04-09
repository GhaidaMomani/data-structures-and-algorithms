

from stack_queue_pseudo.stack_queue_pseudo import Node, Stack, PseudoQueue
import pytest

@pytest.fixture
def my_stack():
    stk = Stack()
    values = ['a', 'b','c', 10]
    for el in values:
       stk.push(el)

    return stk


def test_stack1_stack2_exists(my_stack):
    pseudo_q = PseudoQueue(my_stack)
    assert pseudo_q.stk1.peek() == 10
    assert pseudo_q.stk2.peek() == None

def test_enqueue(my_stack):
    pseudo_q = PseudoQueue(my_stack)
    pseudo_q.enqueue('cat')
    assert pseudo_q.stk1.peek() == 'cat'

def test_enqueue_empty_stack():
    pseudo_q = PseudoQueue(Stack())
    pseudo_q.enqueue('cat')
    assert pseudo_q.stk1.peek() == 'cat'

def test_dequeue(my_stack):
    pseudo_q = PseudoQueue(my_stack)
    assert pseudo_q.dequeue() == 'a'


# def test_pesudo_dequeue():
#     pseudo = PseudoQueue()
#     pseudo.front = Node(1)
#     pseudo.front.next = Node(2)
#     pseudo.front.next.next = Node(3)
#     pseudo.dequeue() 
#     assert pseudo.peek() == 2


# def test_enqueue_dequeue(my_stack):
#     pseudo_q = PseudoQueue(my_stack)
#     assert pseudo_q.stk1.peek() == 10
#     pseudo_q.enqueue('cat')
#     assert pseudo_q.stk1.peek() == 'cat'
#     pseudo_q.enqueue('dog')
#     assert pseudo_q.stk1.peek() == 'dog'
#     assert pseudo_q.dequeue() == 'a'
#     assert pseudo_q.stk1.peek() == 'dog'
#     assert pseudo_q.dequeue() == 'b'
#     assert pseudo_q.stk1.peek() == 'dog'
#     assert pseudo_q.dequeue() == 'c'
#     assert pseudo_q.dequeue() == 10
#     assert pseudo_q.dequeue() == 'cat'
#     assert pseudo_q.dequeue() == 'dog'

# def test_dequeue_empty():
#     pseudo_q = PseudoQueue(Stack())
#     with pytest.raises(Exception):  
#         result = pseudo_q.dequeue()




