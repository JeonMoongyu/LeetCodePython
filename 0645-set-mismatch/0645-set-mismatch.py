class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        check = [1] * (n+1)
        out = []
        for num in nums:
            if check[num] == 0:
                out.append(num)
            check[num] -= 1
        return out + [check[1:].index(1)+1]