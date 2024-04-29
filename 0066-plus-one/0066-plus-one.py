class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for d in digits:
            num = 10 * num + d
        num += 1
        return list(map(int, str(num)))