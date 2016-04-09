#quicksort

import random

def quicksort(n):
    if n <= [1]:
        return n
    else:
        pivot = random.choice(n)
        print(pivot)
        for x in range(0, len(n)):
            if x > pivot:
                for i in reversed(range(0, len(n))):
                    if i < pivot:
                        n[x], n[i] = n[i], n[x]
                        print(n)
                        quicksort(n)



quicksort([4, 3,1, 2, 5])
