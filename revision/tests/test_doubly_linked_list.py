# pytest rather than unittest this time
# missing tests: overlap with singly_linked_list.py

import pytest  # otherwise can't use e.g. with pytest.raises()

from linked_lists.doubly_linked_list import LinkedList


def test_getitem():
    built_in_list = [0, 1, 2, 3, 4, 5]
    linked_list = LinkedList(built_in_list)
    # test integers
    for i in range(6):
        assert built_in_list[i] == linked_list[i]
    # test slices
    assert built_in_list[:3] == linked_list[:3]
    assert built_in_list[3:] == linked_list[3:]
    assert built_in_list[10:] == linked_list[10:]
    assert built_in_list[:10:2] == linked_list[:10:2]
    assert built_in_list[::3] == linked_list[::3]
    # test error handling. note different syntax
    with pytest.raises(IndexError):
        linked_list[7]
    with pytest.raises(TypeError):
        linked_list["spam"]
    linked_list = LinkedList()
    with pytest.raises(IndexError):
        linked_list[0]


def test_delitem():
    linked_list = LinkedList([0, 1, 2, 3, 4])
    # left end
    del linked_list[0]
    assert linked_list[0] == 1
    assert linked_list.head.value == 1
    assert len(linked_list) == 4
    # right end
    del linked_list[3]
    assert linked_list.tail.value == 3
    assert len(linked_list) == 3
    # mid-list
    del linked_list[1]
    assert linked_list[1] == 3
    assert len(linked_list) == 2


def test_add():
    pass


def test_mul():
    pass


def test_append():
    # empty
    linked_list = LinkedList()
    linked_list.append(0)
    assert linked_list.head.value == 0
    assert linked_list.tail.value == 0
    assert len(linked_list) == 1
    # not empty
    linked_list.append(1)
    assert linked_list.head.value == 0
    assert linked_list.tail.value == 1
    assert len(linked_list) == 2


def test_appendleft():
    # empty
    linked_list = LinkedList()
    linked_list.appendleft(0)
    assert linked_list.head.value == 0
    assert linked_list.tail.value == 0
    assert len(linked_list) == 1
    # not empty
    linked_list.appendleft(1)
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 0
    assert len(linked_list) == 2


def test_pop():
    # empty
    linked_list = LinkedList()
    with pytest.raises(IndexError):
        linked_list.pop()
    # one item list
    linked_list = LinkedList([0])
    popped = linked_list.pop()
    assert popped == 0
    assert linked_list.head is None
    assert linked_list.tail is None
    assert len(linked_list) == 0
    # longer list
    linked_list = LinkedList([0, 1, 2, 3, 4, 5])
    # no index provided, i.e. right end
    popped = linked_list.pop()
    assert popped == 5
    assert linked_list.tail.value == 4
    assert len(linked_list) == 5
    # index provided
    popped = linked_list.pop(2)
    assert popped == 2
    assert len(linked_list) == 4
    # index 0, i.e. left end
    popped = linked_list.pop(0)
    assert popped == 0
    assert linked_list.head.value == 1
    assert len(linked_list) == 3


def test_popleft():
    # empty list
    linked_list = LinkedList()
    with pytest.raises(IndexError):
        linked_list.popleft()
    # longer list
    linked_list = LinkedList([0, 1, 2])
    popped = linked_list.popleft()
    assert popped == 0
    assert linked_list.head.value == 1
    assert len(linked_list) == 2


def test_insert():
    # empty
    linked_list = LinkedList()
    linked_list.insert(10, 1)
    assert linked_list[0] == 1
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 1
    assert len(linked_list) == 1
    # left end
    linked_list.insert(0, 0)
    assert linked_list[0] == 0
    assert linked_list.head.value == 0
    assert linked_list.tail.value == 1
    assert len(linked_list) == 2
    # right end
    linked_list.insert(10, 3)
    assert linked_list[2] == 3
    assert linked_list.head.value == 0
    assert linked_list.tail.value == 3
    assert len(linked_list) == 3
    # mid-list
    linked_list.insert(2, 2)
    assert linked_list[2] == 2
    assert linked_list.head.value == 0
    assert linked_list.tail.value == 3
    assert len(linked_list) == 4
    # test node pointers
    assert linked_list[::] == [0, 1, 2, 3]


def test_remove():
    linked_list = LinkedList([0, 1, 2, 3])
    # value not in LinkedList
    with pytest.raises(ValueError):
        linked_list.remove(4)
    # right end
    linked_list.remove(3)
    assert linked_list.tail.value == 2
    assert len(linked_list) == 3
    linked_list.remove(1)
    assert linked_list.head.value == 0
    assert linked_list.tail.value == 2
    assert len(linked_list) == 2
    # left end
    linked_list.remove(0)
    assert linked_list.head.value == 2
    assert len(linked_list) == 1
    # one item list
    linked_list.remove(2)
    assert linked_list.head is None
    assert linked_list.tail is None
    assert len(linked_list) == 0
    # empty list
    with pytest.raises(ValueError):
        linked_list.remove(42)


def test_reverse():
    linked_list = LinkedList([2, 1, 0])
    linked_list.reverse()
    for i in range(3):
        assert i == linked_list[i]
    assert linked_list.head.value == 0
    assert linked_list.tail.value == 2


def test_copy():
    linked_list = LinkedList([0, 1, 2])
    copy_ = linked_list.copy()
    for i in range(3):
        assert copy_[i] == linked_list[i]
    assert copy_.head.value == linked_list.head.value
    assert copy_.tail.value == linked_list.tail.value
    assert len(copy_) == len(linked_list)


def test_count():
    built_in = [1, 1, 1, 2, 2, 3]
    linked_list = LinkedList(built_in)
    for i in range(4):
        assert built_in.count(i) == linked_list.count(i)


def test_extend():
    linked_list = LinkedList([0, 1, 2])
    linked_list.extend(LinkedList([3, 4, 5]))
    assert linked_list.tail.value == 5
    assert len(linked_list) == 6
    linked_list.extend([6, 7, 8])
    assert linked_list.tail.value == 8
    assert len(linked_list) == 9


def test_sum():
    linked_list = LinkedList([0, 1, 2, 3, 4])
    assert linked_list.sum() == 10
    assert linked_list.sum(4) == 4
