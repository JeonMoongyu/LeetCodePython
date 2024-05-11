class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1, dict2 = dict(), dict()
        for num in nums1:
            if num in dict1:
                dict1[num] += 1
            else:
                dict1[num] = 1
        for num in nums2:
            if num in dict2:
                dict2[num] += 1
            else:
                dict2[num] = 1
        out = []
        for num in dict1.keys():
            if num in dict2:
                out += [num] * min(dict1[num], dict2[num])
        return out