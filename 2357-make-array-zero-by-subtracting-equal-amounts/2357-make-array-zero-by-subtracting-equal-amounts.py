class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
        if 0 in seen:
            seen.remove(0)
        return len(seen)