
# factorial - n!

def fact(n):
    if n <= 1:
        return 1
    else:
        return (n * fact(n-1))

# print(fact(5))


# power - xn

def power(x,n):
    m = x
    n = n-1
    while n >= 1:
        x = x*m
        n = n-1
        print(x)

# power(5, 5)


# string reversal


def str_reverse(n):
    return n[::-1]

# print(str_reverse("string"))

# anagrams - return a list of anagrams for a given word

def anagram(n):
    if n == "":
        return [n]
    else:
        answer_set = set()
        for w in anagram(n[1:]):
            for pos in range(len(w)+1):
                answer_set.add(w[:pos]+n[0]+w[pos:])
        return answer_set



# selectionsort
def selection_sort(n):
    for x in range(len(n) -1, 0, -1):
        positionOfMax=0
        for location in range(1,x+1):
            if n[location]>n[positionOfMax]:
                positionOfMax = location
        temp = n[x]
        n[x] = n[positionOfMax]
        n[positionOfMax] = temp

    return n

# quicksort


def main(n):
    pivot = random.choice(n)
    print(pivot)
    for x in range(0, len(n)):
        if x > pivot:
            b = x
            print("b = {}".format(b))
            return
        elif x == pivot:
            print("equal")
            return
    for i in reversed(range(0, len(n))):
        if i < pivot:
            a = i
            print("a = {}".format(a))
            return
        elif i == pivot:
            print("equal")
            return


main([4, 3,1, 2, 5])
