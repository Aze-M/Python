sPos = [1, 0]
hPos = [2, 3]
rCosts = [5, 4, 3]
cCosts = [8, 2, 6, 7]

class Solution:
    def minCost(self, startPos: list[int], homePos: list[int], rowCosts: list[int], colCosts: list[int]) -> int:
        intRowMovement = homePos[0] - startPos[0]
        intColMovement = homePos[1] - startPos[1]

        curPos = startPos
        totalCost = 0

        while intRowMovement != 0:
            if curPos[0] != homePos[0] and intRowMovement > 0:
                curPos[0] += 1
                totalCost += rowCosts[curPos[0]]
                intRowMovement-=1

            elif curPos[0] != homePos[0] and intRowMovement < 0:
                curPos[0] -= 1
                totalCost += rowCosts[curPos[0]]
                intRowMovement+=1

        while intColMovement != 0:
            if curPos[1] != homePos[1] and intColMovement > 0:
                curPos[1] += 1
                totalCost += colCosts[curPos[1]]
                intColMovement-=1

            elif curPos[1] != homePos[1] and intColMovement < 0:
                curPos[1] -= 1
                totalCost += colCosts[curPos[1]]
                intColMovement+=1

        return totalCost

Solution.minCost(Solution, sPos , hPos , rCosts , cCosts )