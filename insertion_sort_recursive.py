def insertionSort(A,l):
    if l <= 1:
        return
    insertionSort(A,l-1)
    key = A[l-1]
    j = l-2
    while j>=0 and key < A[j]:
        A[j+1] = A[j]
        A[j] = key
        j-=1

A = [13, 7, 6, 45, 21, 9, 101, 102]
l =  len(A)
insertionSort(A,l)
print(A)