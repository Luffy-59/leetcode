class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0

        for price in prices:
            if price < lowest:
                lowest = price 
            
            todays_profile = price - lowest 
            if todays_profile > profit :
                profit = todays_profile

        return profit