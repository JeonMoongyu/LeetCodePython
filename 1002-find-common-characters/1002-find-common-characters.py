class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        M_out = dict()
        for c in words[0]:
            if c in M_out:
                M_out[c] += 1
            else:
                M_out[c] = 1
        for word in words[1:]:
            M_curr = dict()
            for c in word:
                if c in M_curr:
                    M_curr[c] += 1
                else:
                    M_curr[c] = 1
            for c in M_out.keys():
                if c in M_curr:
                    M_out[c] = min(M_out[c], M_curr[c])
                else:
                    M_out[c] = 0
        out = []
        for c in M_out.keys():
            out += [c] * M_out[c]
        return out