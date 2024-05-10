class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        cand = []
        for i in range(len(number)):
            if number[i] == digit:
                cand.append(int(number[:i] + number[i+1:]))
        return str(max(cand))