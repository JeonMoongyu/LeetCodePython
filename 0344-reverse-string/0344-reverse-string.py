class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        len_s = len(s)
        for i in range(len_s//2):
            s[i], s[len_s - i - 1] = s[len_s - i - 1], s[i]
            