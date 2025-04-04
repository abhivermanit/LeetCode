
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums) # ( O(1) ) (constant time) because getting the length of a list is a direct operation.
        sum_expected = n * (n + 1) // 2  # ( O(1) ) (constant time) because it involves a fixed number of arithmetic operations regardless of the size of ( n ).
        sum_actual = sum(nums)           # ( O(n) ) (linear time) because it requires iterating through all ( n ) elements in the list to compute the sum.
        return sum_expected - sum_actual # ( O(1) ) (constant time) because it involves a single arithmetic operation.

{Time Complexity} = O(n)


- Arithmetic operations are all linear 
- iterating through the list once is linear 
- finding the length is a one time operation
- append is a one time operation hence linear



def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    for i in range(len(nums)): # This goes through the list once O(n) 
        temp = abs(nums[i]) - 1
        if nums[temp] > 0:
            nums[temp] *= -1

    res = []
    for i, n in enumerate(nums): #This also goes through the entire list O(n) 
        if n > 0:
            res.append(i + 1)

    return res

{Time Complexity} = O(n)




def twoSum(nums, target):
    # Create a dictionary to store the difference (complement) and its index
    num_map = {}
    
    # Loop through the list of numbers
    for i, num in enumerate(nums):
        # Calculate the complement (the number that when added to num gives target)
        complement = target - num
        
        # If the complement exists in the dictionary, we've found the pair
        if complement in num_map:
            # Return the indices of the two numbers
            return [num_map[complement], i]
        
        # Otherwise, store the current number and its index in the dictionary
        num_map[num] = i
    
    # If no solution is found (though problem guarantees one solution)
    return None





