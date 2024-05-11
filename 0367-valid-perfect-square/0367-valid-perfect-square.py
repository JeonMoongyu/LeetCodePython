class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        i = 2
        while i*i <= num :
            if num % (i*i) == 0:
                return self.isPerfectSquare(num//(i*i))
            else:
                i += 1
        return False