
from doubly_linked_list import LinkedList


def remove_duplicates(ll):
    if not ll.head:
        return 
    nodes = set()
    node = ll.head
    while node.next:
        if node.value not in nodes:
            nodes.add(node.value)
            node = node.next
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node = node.next
    # last node 
    if node.value in nodes:
        node.prev.next = None


def kth_to_last(ll, k):
    """Return the kth to last element of a singly linked list."""
    # assume singly linked 
    left = ll.head 
    right = ll.head
    for i in range(k - 1):
        right = right.next 
    while right.next:
        left = left.next 
        right = right.next 
    return left.value 


def partition(ll, x):
    """Arranges ll such that all nodes of value < x come before all nodes of value >= x."""
    # concatenate three lists: < value, == value, > value
    less = LinkedList()
    equal = LinkedList()
    more = LinkedList()
    while ll.head:
        popped = ll.popleft()
        if popped < x:
            less.append(popped)
        elif popped == x:
            equal.append(popped)
        else:
            more.append(popped)
    less.tail.next = equal.head
    equal.tail.next = more.head
    ll.head = less.head
    ll.tail = more.tail


def sum_lists(first, second):
    # e.g. [7, 1, 6] + [5, 9, 2] = [2, 1, 9]
    # (617 + 295 = 912)
    result = LinkedList()
    first = first.head 
    second = second.head
    carry = 0
    while first and second:
        summed = first.value + second.value
        if summed < 10:
            result.append(summed + carry)
            carry = 0
        else:
            result.append(summed % 10 + carry)
            carry = 1 
        first = first.next 
        second = second.next 
    while first:
        result.append(first.value + carry)
        carry = 0 
        first = first.next 
    while second:
        result.append(second.value + carry) 
        carry = 0
        second = second.next
    return result


def intersect(first, second):
    """Returns the node at which the first and second LinkedLists merge."""
    # can't be bothered 
    # see here https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/