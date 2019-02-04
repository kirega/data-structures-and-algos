
"""
HOW IT WORKS

12, 11, 13, 5, 6

Let us loop for i = 1 (second element of the array) to 5 (Size of input array)

i = 1. Since 11 is smalle r than 12, move 12 and insert 11 before 12
11, 12, 13, 5, 6

i = 2. 13 will remain at its position as all elements in A[0..I-1] are smaller 
than 13
11, 12, 13, 5, 6

i = 3. 5 will move to the beginning and all other elements from 11 to 13 will 
move one position ahead of their current position.
5, 11, 12, 13, 6

i = 4. 6 will move to position after 5, and elements from 11 to 13 will move 
one position ahead of their current position.
5, 6, 11, 12, 13

Time Complexity: O(n*2)

Auxiliary Space: O(1)

Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted
in reverse order. And it takes minimum time (Order of n) when elements are already sorted.

Algorithmic Paradigm: Incremental Approach

Sorting In Place: Yes

Stable: Yes

Online: Yes

Uses: Insertion sort is used when number of elements is small. It can also be 
useful when input array is almost sorted, only few elements are misplaced in 
complete big array.


"""
A = [13, 7, 6, 45, 21, 9, 101, 102]

for i in range(1,len(A)):
    key = A[i]
    j = i-1
    while j>=0 and key < A[j]:
        A[j+1] = A[j]
        A[j] = key
        j-=1
print(A)