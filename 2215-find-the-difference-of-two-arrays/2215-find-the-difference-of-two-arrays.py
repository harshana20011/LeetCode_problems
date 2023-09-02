class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        return (lambda a, b: [a - b, b - a])(set(nums1), set(nums2))

            