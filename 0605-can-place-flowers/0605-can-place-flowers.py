class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev, curr = 0, 0
        length = len(flowerbed)
        out = 0
        
        while prev < length:
            if flowerbed[prev] == 0:    
                prev += 1
            else:
                out += prev // 2
                curr = prev + 1
                break
        
        if prev == length:
            return (length+1)//2 >= n
        
        while curr < length:
            if flowerbed[curr] == 0:
                curr += 1
            else:
                out += (curr - prev - 2) // 2
                prev = curr
                curr += 1
        
        if flowerbed[-1] == 0:
            out += (curr - prev - 1) // 2
        
        return out >= n