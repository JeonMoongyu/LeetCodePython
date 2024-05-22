class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        out = 0
        for i in range(len(cost)):
            if i % 3 == 2:
                continue
            out += cost[i]
        return out