def shellSort(A) :
    H = gapSequence(len(A))
    for h in H :
        for k in range(h) :
            stepInsertionSort(A, k, h)
    
def stepInsertionSort(A, k:int, h:int) :
    for i in range(k + h, len(A), h) :
        j = i - h
        newItem = A[i]

        while 0 <= j and newItem < A[j] :
            A[j + h] = A[j]
            j -= h
        A[j + h] = newItem

def gapSequence(n:int) -> list :    # CAN DEFINE VARY
    H = [1]; gap = 1                # {1, 4, 10, 23, 57, 132, 301, 701, 1750} is may best
    while gap < n / 5 :             # After 1750 : G_n = (G_(n-1)) *2.25 로 표현된다.
        gap = 3 * gap + 1
        H.append(gap)
    H.reverse()
    return H
