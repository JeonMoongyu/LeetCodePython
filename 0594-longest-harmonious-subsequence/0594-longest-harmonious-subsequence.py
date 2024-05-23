from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        out = 0
        for num in cnt.keys():
            if num+1 in cnt:
                out = max(out, cnt[num]+cnt[num+1])
        return out