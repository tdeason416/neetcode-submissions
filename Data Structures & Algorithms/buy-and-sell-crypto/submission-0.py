class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        buy = prices[0]
        sell = prices[0]
        for price in prices[1:]:
            if price > sell:
                sell = price
                prof = sell - buy
                print(f"I bought at {buy} and sold at {sell}")
                if prof > max_prof:
                    max_prof = prof
            if price < buy:
                buy = price
                sell = price
        return max_prof
            
            
        