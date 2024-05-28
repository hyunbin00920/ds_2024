import random

def quickEvenSort(A, p:int, r:int) :
    if p < r :
        q = partition(A, p, r)
        quickEvenSort(A, p, q-1)
        quickEvenSort(A, q+1, r)

def partition(A, p:int, r:int) -> int :
    random_element = random.randint(p,r)
    A[random_element], A[r] = A[r], A[random_element]

    x = A[r]
    i = p - 1
    flag = 0
    for j in range(p,r) :
        if A[j] < x :
            i += 1
            A[i], A[j] = A[j], A[i]
        elif A[j] == x :
            if flag == 1 :
                i += 1
                A[i], A[j] = A[j], A[i]
                flag = 0
            else :
                flag = 1

    A[i+1], A[r] = A[r], A[i+1]
    return i+1



