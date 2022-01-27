import pytest

from linked_lists.circular_doubly_linked_list import CircularLinkedList


def test_contains():
    cll = CircularLinkedList([0, 1, 2])
    assert -1 not in cll
    for i in range(3):
        assert i in cll
    assert 3 not in cll


def test_traverse():
    cll = CircularLinkedList([0, 1, 2])
    assert cll.traverse() == [0, 1, 2]
    assert cll.traverse(reverse=True) == [0, 2, 1]


def test_insert():
    # empty list
    cll = CircularLinkedList()
    cll.insert(10, 2)
    assert cll.head.value == 2
    assert cll.head.next == cll.head
    assert cll.head.prev == cll.head
    # replace head
    cll.insert(0, 0)
    assert cll.head.value == 0
    assert cll.traverse() == [0, 2]
    # elsewhere
    cll.insert(1, 1)
    assert cll.traverse() == [0, 1, 2]


def test_remove():
    cll = CircularLinkedList([0, 1, 2])
    with pytest.raises(ValueError):
        cll.remove(3)
    # remove head
    cll.remove(0)
    assert cll.head.value == 1
    assert cll.traverse() == [1, 2]
    # remove elsewhere
    cll.remove(2)
    assert cll.traverse() == [1]
    # one node list
    cll.remove(1)
    assert cll.head == None
    # empty list
    with pytest.raises(ValueError):
        cll.remove(1)


def test_clear():
    cll = CircularLinkedList([0, 1, 2])
    cll.clear()
    assert cll.head == None
