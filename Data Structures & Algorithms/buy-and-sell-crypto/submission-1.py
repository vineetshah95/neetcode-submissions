class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r =0, 1
        maxPrice = 0
        price = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                price = prices[r] - prices[l]
                print(price)
                maxPrice = max(maxPrice, price)
                r += 1
                # l += 1
        return maxPrice
            

