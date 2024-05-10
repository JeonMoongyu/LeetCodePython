class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        out = []
        for i in range(len(s)//k):
            out.append(s[i*k:(i+1)*k])
        out.append(s[(len(s)//k)*k:len(s)])
        for j in range(0,len(out),2):
            out[j] = out[j][::-1]
        return ''.join(out)