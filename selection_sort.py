
"""
The selection sort algorithm sorts an array by repeatedly finding the
minimum element (considering ascending order) from unsorted part and
putting it at the beginning. The algorithm maintains two subarrays in
 a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering
ascending order) from the unsorted subarray is picked and moved to the
sorted subarray.

Time Complexity: O(n2) as there are two nested loops.
Auxiliary Space: O(1) The good thing about selection sort is it never makes 
more than O(n) swaps and can be useful when memory write is a costly operation.
"""
A = [64, 25, 12, 22, 11]
print(A)
for i in range(len(A)): 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
    A[i], A[min_idx] = A[min_idx], A[i] 

print(A)
