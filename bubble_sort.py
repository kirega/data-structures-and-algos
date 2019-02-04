"""
Bubble Sort is the simplest sorting algorithm that works by repeatedly 
swapping the adjacent elements if they are in wrong order.

The above function always runs O(n^2) time even if the array is sorted. 
It can be optimized by stopping the algorithm if inner loop didn’t cause any swap.

Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.

Best Case Time Complexity: O(n). Best case occurs when array is already sorted.

Auxiliary Space: O(1)

Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are already sorted.

Sorting In Place: Yes

Stable: Yes
"""
A = [64, 25, 12, 22, 11]

for j in range(len(A)):
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]

print(A)

# Optimized bubble sort, checks if any swap was made and exits if none was made
for j in range(len(A)):
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
            swapped = True
    if swapped == False: 
            break

