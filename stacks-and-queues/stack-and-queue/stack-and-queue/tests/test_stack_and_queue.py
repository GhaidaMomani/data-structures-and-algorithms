
import pytest
from stack_and_queue.stack_and_queue import Node, Stack, Queue

def test_Node_exists():
    assert Node("test")


# Stack Tests
def test_Stack_exists():
    assert Stack()


def test_Stack_push_one_item():
    stk = Stack()
    stk.push(1)
    actual = stk.peek()
    expected = 1
    assert actual == expected


def test_Stack_push_multiple_items():
    my_stack.push(2)
    my_stack.push(3)
    actual = my_stack.peek()
    expected = 3
    assert actual == expected




def test_Stack_pop_one_item():
    stk = Stack()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    actual = stk.pop()
    expected = 3
    assert actual == expected


def test_Stack_pop_multiple_items():
    stk = Stack()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    stk.pop()
    actual = stk.pop()
    expected = 2
    assert actual == expected





def test_Stack_peek_top():
    stk = Stack()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    actual = stk.peek()
    expected = 3
    assert actual == expected


def test_Stack_isEmpty_empty():
    stk = Stack()
    actual = stk.is_empty()
    expected = True
    assert actual == expected


def test_Stack_isEmpty_not_empty():
    stk = Stack()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    actual = stk.is_empty()
    expected = False
    assert actual == expected


# Queue Tests
def test_Queue_exists():
    assert Queue()


def test_Queue_enqueue_one_item():
    queue = Queue()
    queue.enqueue(1)
    actual = queue.peek()
    expected = 1
    assert actual == expected


def test_Queue_enqueue_multiple_items():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    actual = q.peek()
    expected = 1
    assert actual == expected


def test_Queue_dequeue_one_item():
    q = Queue()
    q.enqueue(1)
    actual = q.dequeue()
    expected = 1
    assert actual == expected


def test_Queue_dequeue_multiple_items():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
    actual = q.dequeue()
    expected = 2
    assert actual == expected


def test_Queue_peek_front():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    actual = q.peek()
    expected = 1
    assert actual == expected




def test_Queue_isEmpty_empty():
    q = Queue()
    actual = q.is_empty()
    expected = True
    assert actual == expected


def test_Queue_isEmpty_not_empty():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    actual = q.is_empty()
    expected = False
    assert actual == expected






# def test_queue_enqueu():
#     test_queue = Queue()
#     assert test_queue.front == None
#     test_queue.enqueue(3)
#     assert test_queue.front.value == 3
#     test_queue.enqueue('b')
#     assert test_queue.rear.value == 'b'
#     assert test_queue.front.value == 3
#     test_queue.enqueue('c')
#     assert test_queue.rear.value == 'c'
#     assert test_queue.front.value == 3

# def test_queue_dequeue():
#     test_queue = create_queue(['a', 'b', 'c', 'd'])
#     assert test_queue.dequeue() == 'a'
#     assert test_queue.front.value == 'b'
#     assert test_queue.front.next.value == 'c'
#     test_queue.dequeue()
#     test_queue.dequeue()
#     test_queue.dequeue()
#     assert test_queue.peek() == None


