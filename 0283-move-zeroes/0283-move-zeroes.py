class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero_count = 0

       
        for num in nums:
            if num != 0:
                nums[non_zero_count] = num
                non_zero_count += 1
        
       
        while non_zero_count < len(nums):
            nums[non_zero_count] = 0
            non_zero_count += 1