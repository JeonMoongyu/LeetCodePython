class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        curr_max = arr[-1]
        for i in range(n-2, -1, -1):
            temp = arr[i]
            arr[i] = curr_max
            curr_max = max(curr_max, temp)
        arr[-1] = -1
        return arr