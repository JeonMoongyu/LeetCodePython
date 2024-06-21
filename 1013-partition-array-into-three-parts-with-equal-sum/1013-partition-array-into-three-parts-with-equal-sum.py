class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sumAll = sum(arr)
        if sumAll % 3 != 0:
            return False
        sumEach = sumAll // 3
        
        sum1 = 0
        for i in range(len(arr)-2):
            sum1 += arr[i]
            if sum1 == sumEach:
                break
        if sum1 != sumEach:
            return False
        
        sum2 = 0
        for j in range(i+1, len(arr)-1):
            sum2 += arr[j]
            if sum2 == sumEach:
                return True
        return False