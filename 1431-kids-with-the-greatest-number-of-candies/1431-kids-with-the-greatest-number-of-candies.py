class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_num_init = max(candies)
    
        candies_bool = []
        for candy in candies:
                if candy + extraCandies >= max_num_init:
                        candies_bool.append(True)
                else:
                        candies_bool.append(False)
                
        return candies_bool