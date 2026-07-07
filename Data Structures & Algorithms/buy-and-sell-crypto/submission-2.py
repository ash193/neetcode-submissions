class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #left is buying(look for lowest price) & right is selling(look for highest sell price)
        left, right = 0, 1 
        maxP = 0 #theres no current profit atm

        while right < len(prices): #this makes sure right is within the bounds of prices
            #if we found low buy price and high sell price we would make a profit here
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
            else:
                left = right #otherwise the low price left is found where right is at
            right += 1 #we want the sell price to transition through the array
        
        return maxP

