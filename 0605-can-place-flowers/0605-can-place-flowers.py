class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True 
        
        count = 0
        flowerbed_size = len(flowerbed)
        
        for i in range(flowerbed_size):
            if flowerbed[i] == 0:
                if i == 0 or flowerbed[i - 1] == 0:
                    if i == flowerbed_size - 1 or flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        count += 1
                        if count >= n:
                            return True
        
        return False
