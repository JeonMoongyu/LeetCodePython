class Solution:
    def digitCount(self, num: str) -> bool:
        cnt = {}
        for i in num:
            if int(i) in cnt:
                cnt[int(i)] += 1
            else:
                cnt[int(i)] = 1
        for i in range(len(num)):
            if (i in cnt and int(num[i]) != cnt[i]) or (i not in cnt and int(num[i]) != 0):
                return False
        return True