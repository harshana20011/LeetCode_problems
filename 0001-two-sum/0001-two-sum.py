class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        positions = []
        for position, number in enumerate(nums):
            second_number = target - number
            if second_number in nums and nums.index(second_number) != position:
                positions.append(position)
                positions.append(nums.index(second_number))
                break  
        
        return positions
        