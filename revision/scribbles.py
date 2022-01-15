from random import randint


l1 = [randint(-9, 9) for i in range(10)].sort()
l2 = [randint(-9, 9) for i in range(10)].sort()

# merge these recursively, for the challenge

def merge(l1, l2):
    merged = []
    if l1[0] < l2[0]:
        merged.append(l1[0])