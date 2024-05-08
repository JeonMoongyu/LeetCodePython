class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        out = []
        for freq, val in zip(nums[::2], nums[1::2]):
            out += [val] * freq
        return out