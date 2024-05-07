class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        M = dict()
        for num in nums:
            if num % 2 == 0:
                if num in M:
                    M[num] += 1
                else:
                    M[num] = 1
        if not M:
            return -1
        return sorted(M.keys(), key = lambda x: (-M[x], x))[0]
        