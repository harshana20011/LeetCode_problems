class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        b = 1
        c = 1
        if n == 0:
            return 0 
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            for i in range(n-2):  
                d = a + b + c
                a, b, c = b, c, d  
            return d
