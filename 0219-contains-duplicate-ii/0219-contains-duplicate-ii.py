class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = dict()
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = i
            elif i - seen[nums[i]] <= k:
                return True
            else:
                seen[nums[i]] = i
        return False