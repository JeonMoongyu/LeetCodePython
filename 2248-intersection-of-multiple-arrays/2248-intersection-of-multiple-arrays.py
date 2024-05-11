class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        set_list = [ set(arr) for arr in nums ]
        out_set = set.intersection(*set_list)
        return sorted(list(out_set))