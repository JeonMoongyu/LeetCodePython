class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        arr = [ [i, score[i]] for i in range(n) ]
        # print(arr)
        arr.sort(key= lambda x: -x[1])
        # print(arr)
        arr[0][1] = "Gold Medal"
        if n >= 2:
            arr[1][1] = "Silver Medal"
        if n >= 3:
            arr[2][1] = "Bronze Medal"
        for j in range(3, n):
            arr[j][1] = str(j+1)
        arr.sort(key = lambda x: x[0])
        return [arr[i][1] for i in range(n)]