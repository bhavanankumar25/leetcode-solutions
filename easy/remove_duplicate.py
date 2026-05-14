class Solution:
    def removeDuplicates(self, nums):
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:  # found a new unique number
                nums[k] = nums[i]     # place it at position k
                k += 1                 
        return k   
    

#k = position where next unique element should go (starts at 1)
