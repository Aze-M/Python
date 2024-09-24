class Solution:
    def mySqrt(self, x: int) -> int:
        maxdiv = 0
        for div in range(0,x+1):
            if div * div == x:
                return div
            elif div*div < x:
                maxdiv = div
            elif div*div > x:
                return maxdiv
        return x
            
sol = Solution

ans1 = sol.mySqrt(sol, 8)
ans2 = sol.mySqrt(sol, 4)
ans3 = sol.mySqrt(sol, 2)