# create min heap
# extract root repeatedly
# redo heap class, last was awful
# try heapq?

import heapq
from random import randint


li = [randint(0, 8) for i in range(8)]
print(f"{li=}")


def heapsort(li):
    heapq.heapify(li)
    return [heapq.heappop(li) for i in range(len(li))]


print(heapsort(li))

# much easier
