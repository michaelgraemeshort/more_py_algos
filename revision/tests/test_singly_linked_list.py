# NOTE TO SELF: cd into more_py_algos/revision, then run python3 -m unittest tests/test_singly_linked_list.py
# if in more_py_algos as usual, python3 -m unittest revision/tests/test_singly_linked_list.py DOES NOT work
# the -m flag runs the module specified thereafter as a script
# edge cases here: empty list, ends of list
# check head, tail and length are handled correctly
# todo: test error handling


import unittest

from linked_lists.singly_linked_list import (
    LinkedList,
)  # might alter this file structure. also, Black is responsible for this weird formatting


class SinglyLinkedListTests(unittest.TestCase):
    def test_getitem(self):
        built_in_list = [0, 1, 2, 3, 4, 5]
        linked_list = LinkedList(built_in_list)
        # test integers
        for i in range(6):
            self.assertEqual(built_in_list[i], linked_list[i])
        # test slices
        self.assertEqual(built_in_list[:3], linked_list[:3])
        self.assertEqual(built_in_list[3:], linked_list[3:])
        self.assertEqual(built_in_list[10:], linked_list[10:])
        self.assertEqual(built_in_list[:10:2], linked_list[:10:2])
        self.assertEqual(built_in_list[::3], linked_list[::3])
        # test error handling. note weird syntax
        with self.assertRaises(IndexError):
            linked_list[7]
        with self.assertRaises(TypeError):
            linked_list["spam"]
        linked_list = LinkedList()
        with self.assertRaises(IndexError):
            linked_list[0]

    # ^^ this all counts as 1 test in the report
    # and if the first assertion fails, the others won't run

    def test_delitem(self):
        linked_list = LinkedList([0, 1, 2, 3, 4])
        # left end
        del linked_list[0]
        self.assertEqual(linked_list[0], 1)
        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.length, 4)
        # right end
        del linked_list[3]
        self.assertEqual(linked_list[2], 3)
        self.assertEqual(linked_list.tail.value, 3)
        self.assertEqual(linked_list.length, 3)
        # mid-list
        del linked_list[1]
        self.assertEqual(linked_list[1], 3)
        self.assertEqual(linked_list.length, 2)

    def test_add(self):
        # both empty
        left = LinkedList()
        right = LinkedList()
        added = left + right
        self.assertIsNone(added.head)
        self.assertIsNone(added.tail)
        self.assertEqual(added.length, 0)
        # right empty
        left = LinkedList([0, 1, 2])
        added = left + right
        self.assertEqual(added.head.value, 0)
        self.assertEqual(added.tail.value, 2)
        self.assertEqual(added.length, 3)
        # left empty
        left = LinkedList()
        right = LinkedList([3, 4, 5])
        added = left + right
        self.assertEqual(added.head.value, 3)
        self.assertEqual(added.tail.value, 5)
        self.assertEqual(added.length, 3)
        # neither empty
        left = LinkedList([0, 1, 2])
        added = left + right
        self.assertEqual(added.head.value, 0)
        self.assertEqual(added.tail.value, 5)
        self.assertEqual(added.length, 6)

    def test_mul(self):
        left = LinkedList([0, 1, 2])
        right = 0
        multiplied = left * right
        self.assertIsNone(multiplied.head)
        self.assertIsNone(multiplied.tail)
        self.assertEqual(multiplied.length, 0)
        for right in range(1, 4):
            multiplied = left * right
            self.assertEqual(multiplied.head.value, 0)
            self.assertEqual(multiplied.tail.value, 2)
            self.assertEqual(multiplied.length, left.length * right)

    def test_append(self):
        linked_list = LinkedList()
        # empty
        linked_list.append(0)
        self.assertEqual(linked_list.head.value, 0)
        self.assertEqual(linked_list.tail.value, 0)
        self.assertEqual(linked_list.length, 1)
        # not empty
        linked_list.append(1)
        self.assertEqual(linked_list.head.value, 0)
        self.assertEqual(linked_list.tail.value, 1)
        self.assertEqual(linked_list.length, 2)

    def test_appendleft(self):
        linked_list = LinkedList()
        # empty
        linked_list.appendleft(0)
        self.assertEqual(linked_list.head.value, 0)
        self.assertEqual(linked_list.tail.value, 0)
        self.assertEqual(linked_list.length, 1)
        # not empty
        linked_list.appendleft(1)
        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.tail.value, 0)
        self.assertEqual(linked_list.length, 2)

    def test_pop(self):
        # empty
        linked_list = LinkedList()
        with self.assertRaises(IndexError):
            linked_list.pop()
        # one item list
        linked_list = LinkedList([0])
        popped = linked_list.pop()
        self.assertEqual(popped, 0)
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)
        self.assertEqual(linked_list.length, 0)
        # longer list
        linked_list = LinkedList([0, 1, 2, 3, 4, 5])
        # no index provided, i.e. right end
        popped = linked_list.pop()
        self.assertEqual(popped, 5)
        self.assertEqual(linked_list.tail.value, 4)
        self.assertEqual(linked_list.length, 5)
        # index provided
        popped = linked_list.pop(2)
        self.assertEqual(popped, 2)
        self.assertEqual(linked_list.length, 4)
        # index 0, i.e. left end
        popped = linked_list.pop(0)
        self.assertEqual(popped, 0)
        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.length, 3)

    def test_popleft(self):
        # empty list
        linked_list = LinkedList()
        with self.assertRaises(IndexError):
            linked_list.popleft()
        # one item list NOT tested - just calls pop, tested above
        # longer list
        linked_list = LinkedList([0, 1, 2])
        popped = linked_list.popleft()
        self.assertEqual(popped, 0)
        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.length, 2)

    def test_index(self):
        linked_list = LinkedList([0, 1, 2])
        for i in range(3):
            self.assertEqual(i, linked_list[i])

    def test_insert(self):
        # empty list
        linked_list = LinkedList()
        linked_list.insert(10, 0)
        self.assertEqual(linked_list[0], 0)
        self.assertEqual(linked_list.length, 1)
        self.assertEqual(linked_list.head.value, 0)
        self.assertEqual(linked_list.tail.value, 0)
        # left end
        linked_list = LinkedList([1, 2])
        linked_list.insert(0, 0)
        self.assertEqual(linked_list[0], 0)
        self.assertEqual(linked_list.length, 3)
        self.assertEqual(linked_list.head.value, 0)
        # right end
        linked_list.insert(3, 3)
        self.assertEqual(linked_list[3], 3)
        self.assertEqual(linked_list.length, 4)
        self.assertEqual(linked_list.tail.value, 3)
        # mid-list
        linked_list.insert(2, 42)
        self.assertEqual(linked_list[2], 42)
        self.assertEqual(linked_list.length, 5)

    def test_remove(self):
        linked_list = LinkedList([0, 1, 2, 3])
        # value not in LinkedList
        with self.assertRaises(ValueError):
            linked_list.remove(4)
        # right end
        linked_list.remove(3)
        self.assertEqual(linked_list.tail.value, 2)
        self.assertEqual(linked_list.length, 3)
        # mid-list
        linked_list.remove(1)
        self.assertEqual(linked_list.head.value, 0)
        self.assertEqual(linked_list.tail.value, 2)
        self.assertEqual(linked_list.length, 2)
        # left end
        linked_list.remove(0)
        self.assertEqual(linked_list.head.value, 2)
        self.assertEqual(linked_list.length, 1)
        # one-item list
        linked_list.remove(2)
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)
        self.assertEqual(linked_list.length, 0)
        # empty list
        with self.assertRaises(ValueError):
            linked_list.remove(42)

    def test_reverse(self):
        linked_list = LinkedList([4, 3, 2, 1, 0])
        linked_list.reverse()
        for i in range(5):
            self.assertEqual(i, linked_list[i])
        self.assertEqual(linked_list.head.value, 0)
        self.assertEqual(linked_list.tail.value, 4)
        self.assertEqual(linked_list.length, 5)

    def test_copy(self):
        linked_list = LinkedList([0, 1, 2])
        copy_ = linked_list.copy()
        for i in range(3):
            self.assertEqual(linked_list[i], copy_[i])
        self.assertEqual(linked_list.head.value, copy_.head.value)
        self.assertEqual(linked_list.tail.value, copy_.tail.value)
        self.assertEqual(linked_list.length, copy_.length)

    def test_count(self):
        built_in = [1, 1, 1, 2, 2, 3]
        linked_list = LinkedList(built_in)
        for i in range(4):
            self.assertEqual(built_in.count(i), linked_list.count(i))

    def test_extend(self):
        linked_list = LinkedList([0, 1, 2])
        linked_list.extend(LinkedList([3, 4, 5]))
        self.assertEqual(linked_list.tail.value, 5)
        self.assertEqual(linked_list.length, 6)
        linked_list.extend([6, 7, 8])
        self.assertEqual(linked_list.tail.value, 8)
        self.assertEqual(linked_list.length, 9)

    def test_sum(self):
        linked_list = LinkedList([0, 1, 2, 3, 4])
        self.assertEqual(linked_list.sum(), 10)
        self.assertEqual(linked_list.sum(4), 4)

    def test_sort(self):
        built_in = [-9, 7, -3, 3, -9, 7, -1, 3, -2, 2]
        linked_list = LinkedList(built_in)
        built_in.sort()
        linked_list = linked_list.sort()
        for i in range(10):
            self.assertEqual(built_in[i], linked_list[i])
        self.assertEqual(linked_list.head.value, -9)
        self.assertEqual(linked_list.tail.value, 7)
        self.assertEqual(linked_list.length, 10)


if __name__ == "__main__":
    unittest.main()
