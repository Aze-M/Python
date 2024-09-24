class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        low, high = 0, num

        while low <= high:
            numtry = (low+high) / 2

            if numtry * numtry == num:
                return True
            elif numtry * numtry < num:
                low = numtry + 1
            elif numtry * numtry > num:
                high= numtry - 1
        
        return False
            
sol = Solution

ans1 = sol.isPerfectSquare(sol, 8)
ans2 = sol.isPerfectSquare(sol, 4)
ans3 = sol.isPerfectSquare(sol, 16)

print(ans1,ans2,ans3)