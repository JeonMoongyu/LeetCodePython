class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(key = lambda x: (x[0], -x[1]))
        curr_st, cnt = 0, 0
        out = []
        for i in range(len(items)):
            if items[i][0] != curr_st:
                avg_score = sum([ items[i+k][1] for k in range(5) ]) // 5 
                out.append((items[i][0], avg_score))
                curr_st = items[i][0]
        return out
        