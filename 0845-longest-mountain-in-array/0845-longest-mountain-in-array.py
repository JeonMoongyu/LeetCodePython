class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        start = 0
        pastPeak = False
        curr = 0
        out = 0
        
        while curr < len(arr):
            if curr == len(arr) - 1:
                if pastPeak:
                    out = max(curr - start + 1, out)
                break
            if (not pastPeak and arr[curr] < arr[curr+1]) or \
               (pastPeak and arr[curr] > arr[curr+1]):
                curr += 1
            elif not pastPeak and curr > 0 and \
                 arr[curr] > arr[curr-1] and arr[curr] > arr[curr+1]:
                pastPeak = True
                curr += 1
            else:
                if pastPeak:
                    out = max(curr - start + 1, out)
                pastPeak = False
                if arr[curr] < arr[curr+1]:
                    start = curr
                    curr = start + 1
                else: # arr[curr] == arr[curr+1]
                    start = curr + 1
                    curr = start
                    
        
        return out if out >= 3 else 0
            
                
            
        
                