# 268. Missing Number

My Approach

class Solution(object):
    def missingNumber(self, nums):
        self.nums = nums # See this is not needed as there is only one function, had there been multiple we would need this instance variable initialization
        nums.sort()
        for i in range(0,len(nums)+1):
            if i in nums:
                continue
            else:
                return i

  Let's optimize this solution :-


# 

