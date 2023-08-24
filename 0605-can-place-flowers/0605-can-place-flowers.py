class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
                return True 
        if n > len(flowerbed):
                print('Enter a number of n flowers to add that is inferior to the number of spots in flowerbed')
        else: 
                sum_adjacent = []
                for spot, _ in enumerate(flowerbed):
                        try:
                                if not (len(flowerbed) >= 1 or len(flowerbed)<= 2 * 10 ** 4 ):
                                        raise ValueError('List is either to short or too long')
                                
                                if not (flowerbed[spot] == 1 or flowerbed[spot]==0):
                                        raise ValueError('The list should contain only zeros and ones')
                                
                                sum_adjacent.append(flowerbed[spot]+ flowerbed[spot+1])
                        except ValueError as e:
                                print(e)
                        except:        
                                sum_adjacent.append(flowerbed[spot]+0)
                print(sum_adjacent) 
                
                for sum in sum_adjacent:
                        if sum > 1:
                                print('Enter a flowerbed without two flowers adjacent')
                                break
                        
                        else:
                                if len(flowerbed) == 1:
                                        
                                        if flowerbed[0] == 1:
                                                return False
                                        else:
                                                return True
                                elif len(flowerbed) == 2:
                                        if n>1:
                                                return False
                                        if flowerbed[0] == 1 or flowerbed[1] == 1:
                                                return False
                                        
                                        else: 
                                                return True 
                                else:
                                        count = 0
                                        for spot in range(len(flowerbed)):
                                                if flowerbed[spot] == 0 and (spot == 0 or flowerbed[spot - 1] == 0) and (spot == len(flowerbed) - 1 or flowerbed[spot + 1] == 0):
                                                        flowerbed[spot] = 1
                                                        count += 1
                                                        if count >= n:
                                                                return True
                                        return False
