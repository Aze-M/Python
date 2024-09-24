# Two armies are fighting eachother, the armies are
# lists of lists that can only be five wide but up to 10^4 long
#
# Armies fight in front first, then diagonally if they still have valid targets
# EG [0,0,3,0,0]
# VS [0,1,0,1,0]
# should result in
# [0,0,2,0,0]
# [0,0,0,0,0]
#
# for this problem the attacking army strikes first, and the function should return 1 for a victory, 0 for a draw, and -1 for a loss.
# the above example would return 1 as the attacking army won.
# regardless of the input the function should never crash, even if given something out of scope or a negative army value such as -1
# 
# Valid Inputs:
# Have a width of 5
# are a list of list containing at least one list
# never have more than 9 soldiers in a segment Such as [0,0,10,0,0] being invalid
# can not have negative soldiers in a segment
# will always result in 1 0 or -1 output
#
# Invalid inputs should return a verbose error, showing what was wrong and where.

def resolve_fight(_att_army: list[list], _def_army: list[list]) -> int:
    pass

army1 = [[1,1,1,1,1],[0,0,1,0,0]]
army2 = [[2,0,1,0,2],[0,0,2,0,0]]
army3 = [[9,9,9,9,9]]
for i in range(99):
    army3.append([int(i/10),int(i/10),int(i/10),int(i/10),int(i/10)])
army4 = [[9,9,9,9,9]]
for i in range(75):
    army4.append([9,9,9,9,9])

resolve_fight(army1, army2) #1
resolve_fight(army3, army4) #1
resolve_fight(army1, [[9,9,9,9,9]]) #-1
resolve_fight([[0,0,0,0,0]], [[0,0,0,0,0]]) #0
resolve_fight([[0,0,9959,0,0]], [[0,0,0,0,0]]) #-1 (for cheated soldier count)
resolve_fight([[0,0,0,0,0]], [[0,0,901,0,0]]) #1 (for cheated soldier count)
resolve_fight([],[]) #0 (invalid inputs)
resolve_fight([1,2,3,2,1],[]) #0 (invalid inputs)
resolve_fight([[1,2,3,2,1],1],[]) #0 (invalid inputs)





