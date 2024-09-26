class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]

        prev_line = [1,1]
        ans : list[int]
        curIndex = 2

        while curIndex < rowIndex+1:
            #buffer new ans
            ans  = []

            #first is 1
            ans.append(1)

            for idx in range(1,curIndex):
                ans.append(prev_line[idx-1]+prev_line[idx])

            #last is also 1
            ans.append(1)

            prev_line = ans
            curIndex+=1

        return ans
    
end = Solution.getRow(Solution, 3)

print(end)






