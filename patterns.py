#1. Prefix Sum pattern

def prefix_sum(arr):
    if not arr:  # Check if array is empty
        return arr
    
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]  # Compute the prefix sum
    
    return arr


# The output of initial array ([1, 2, 3, 4]) is [1, 3, 6, 10].




 #2. Pointers 

- Problems like palindrome, 2 pointers iterate. 

- 3 sum 


#3. Sliding Window 

