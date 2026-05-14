class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            need = target - nums[i]
            for j in range(len(nums)):
                if nums[j] == need and j != i:
                    return [i, j]
                
"""Outer loop - goes through each number one by one
need- calculates what partner number is needed
Inner loop - searches the rest of the list for that partner
j != i - makes sure you don't use the same number twice
return [i, j] - returns both positions

range(len(nums)): len(nums) = 4 ( if there are 4 items)
range(4) = 0, 1, 2, 3 (positions)

So for i in range(len(nums)) means:
i = 0 first loop → nums[0] = 2
i = 1 second loop → nums[1] = 7
i = 2 third loop → nums[2] = 11
i = 3 fourth loop → nums[3] = 15
"""