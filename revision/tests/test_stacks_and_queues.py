import pytest

from stacks_and_queues.stacks_and_queues import (
    ListStack,
    ListQueue,
    LinkedListStack,
    LinkedListQueue,
)


def test_ListStack_push():
    stack = ListStack(1)
    stack.push(0)
    assert stack.stack[0] == 0
    with pytest.raises(IndexError):
        stack.push(1)


def test_ListStack_pop():
    stack = ListStack(1)
    stack.push(0)
    assert stack.pop() == 0
    with pytest.raises(IndexError):
        stack.pop()

def test_ListQueue_enqueue():
    queue = ListQueue(1)
    queue.enqueue(0)
    assert queue.queue[0] == 0
    with pytest.raises(IndexError):
        queue.enqueue(1) 

def test_ListQueue_dequeue():
    queue = ListQueue(1)
    queue.enqueue(0)
    assert queue.dequeue() == 0 
    with pytest.raises(IndexError):
        queue.dequeue()

def test_LinkedListStack_push():
    stack = LinkedListStack(2)
    stack.push(0)
    assert stack.head.value == 0
    assert stack.tail.value == 0
    assert stack.size == 1
    stack.push(1)
    assert stack.tail.value == 1
    assert stack.size == 2 
    with pytest.raises(IndexError):
        stack.push(2)


def test_LinkedListStack_pop():
    stack = LinkedListStack(2)
    stack.push(0)
    stack.push(1)
    assert stack.pop() == 1
    assert stack.head.value == 0 
    assert stack.tail.value == 0
    assert stack.size == 1
    assert stack.pop() == 0 
    assert stack.head == None 
    assert stack.tail == None 
    assert stack.size == 0
    with pytest.raises(IndexError):
        stack.pop()

    
def test_LinkedListStack_is_empty():
    stack = LinkedListStack()
    assert stack.is_empty() == True
    stack.push(0)
    assert stack.is_empty() == False
    

def test_LinkedListQueue_enqueue():
    queue = LinkedListQueue(2)
    queue.enqueue(0)
    assert queue.head.value == 0
    assert queue.tail.value == 0 
    assert queue.size == 1 
    queue.enqueue(1)
    assert queue.tail.value == 1 
    assert queue.size == 2 
    with pytest.raises(IndexError):
        queue.enqueue(2)


def test_LinkedListQueue_dequeue():
    queue = LinkedListQueue(2)
    queue.enqueue(0)
    queue.enqueue(1)
    assert queue.dequeue() == 0 
    assert queue.head.value == 1
    assert queue.tail.value == 1 
    assert queue.size == 1
    assert queue.dequeue() == 1 
    assert queue.head == None 
    assert queue.tail == None 
    assert queue.size == 0
    with pytest.raises(IndexError):
        queue.dequeue()
    
