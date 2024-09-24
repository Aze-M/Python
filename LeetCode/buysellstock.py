class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        lowest = float("inf")
        maxprofit = 0

        #wow
        for price in prices:
            if price < lowest:
                lowest = price
                continue

            maxprofit = max(maxprofit, price - lowest)

                    
        return maxprofit

        

p1 = [7,1,5,3,6,4]
p2 = [2,4,1]

ans = Solution.maxProfit(Solution, p1)
ans2 = Solution.maxProfit(Solution, p2)

print(ans, ans2)