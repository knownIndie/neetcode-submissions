class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r,p=0,1,0

        while r<len(prices):

            val = prices[r] - prices[l]
            
            if prices[r]<prices[l]:
                l=r
            else:
                p = max(p,val)
            r+=1
            
        return p