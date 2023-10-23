class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1 and not flowerbed[0] and n == 1:
            return True

        if len(flowerbed) >= 2 and not (flowerbed[0] + flowerbed[1]):
            flowerbed[0] = 1
            n -= 1
        
        for i in range(1, len(flowerbed)-1):
            if not (flowerbed[i-1] + flowerbed[i] + flowerbed[i+1]):
                flowerbed[i] = 1
                n -= 1
                if not n:
                    break
        

        if len(flowerbed) >= 2 and not (flowerbed[-1] + flowerbed[-2]):
            flowerbed[-1] = 1
            n -= 1
        
        return True if n <= 0 else False
        
