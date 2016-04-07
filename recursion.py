

# quicksort


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
