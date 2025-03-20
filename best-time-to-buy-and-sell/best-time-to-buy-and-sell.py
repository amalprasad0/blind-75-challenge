class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        res=0

        while(r<len(prices)):
            if(prices[r]>prices[l]):
                res=max(res,prices[r]-prices[l])
            else:
                l=r
            r+=1
        return res if res!=0 else 0
# TC=o(n)
# SC=o(1)