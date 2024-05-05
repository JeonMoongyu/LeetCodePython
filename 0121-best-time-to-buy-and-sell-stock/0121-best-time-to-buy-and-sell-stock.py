class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = highest = prices[0]
        out = 0
        for price in prices[1:]:
            if price < lowest:
                lowest = price
                highest = price
            if price > highest:
                highest = price
            out = max(out, highest - lowest)
        return out
            