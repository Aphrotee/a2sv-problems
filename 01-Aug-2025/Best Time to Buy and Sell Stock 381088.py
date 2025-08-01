# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sell = prices[0]
        max_profit = 0
        for price in prices:
            buy = min(buy, price)
            if price - buy > max_profit:
                max_profit = price - buy
        return max_profit