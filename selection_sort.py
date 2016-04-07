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



    # if len(n) <= 1:
    #     return n
    # else:
    #     m =[]
    #     for x in n:
    #         if x <= n[0]:
    #             m.insert(0, x)
    #             n.remove(x)
    #     selection_sort(n)
    #     return m

#
# print(selection_sort(n))
