class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = strs[0]
        for elem in strs[1:]:
            temp = out
            out = ""
            for i in range(min(len(temp), len(elem))):
                if temp[i] != elem[i]:
                    break
                out += temp[i]
        return out