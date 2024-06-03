class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        def findTheWinnerRecursion(left: list, k: int, c: int) -> int:
            if len(left) == 1:
                return left[0]
            n = len(left)
            lost = (c+k-1)%n
            print(left, left[lost])
            return findTheWinnerRecursion(left[:lost]+left[lost+1:], k, lost)
        
        return findTheWinnerRecursion([i for i in range(1,n+1)], k, 0)