class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        def BS(left, right):
            if left > right:
                return left
            mid = (left+right)//2
            if letters[mid] == target:
                return mid
            if letters[mid] > target:
                return BS(left, mid-1)
            if letters[mid] < target:
                return BS(mid+1, right)
            
        n = len(letters)
        k = BS(0, n-1)
        while k < n and letters[k] <= target:
            k += 1
        return letters[0] if k == n else letters[k] 