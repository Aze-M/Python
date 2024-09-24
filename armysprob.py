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

def validate_army(_army: list[list]) -> bool:

    #check we have a list of lists
    try:
        _army[0][0]
    except (IndexError, TypeError):
        print("Army is not list of lists!")
        return False

    if len(_army) < 1:
        print("Army is not at least 1 line.")
        return False
    
    #check for minimum width
    for line in _army:
        #ensure we do not suddenly stop having a list of lists
        if not isinstance(line, list):
            print(f"Invalid input! Encontered non List in army!")
            return False
        
        if len(line) != 5:
            print(f"Invalid input, line {line} is not 5 wide.")
            return False
        
    return True

def do_attack(_atk_num: int, _def_num: int) -> int:
    
    #attack and prevent negative
    _def_num -= _atk_num
    if _def_num < 0:
        _def_num = 0

    return _def_num


def resolve_fight(_att_army: list[list], _def_army: list[list]) -> int:
    
    print("--------")

    print("Testing Attacker army.")
    if not validate_army(_att_army):
        print("Invalid army, resolving to Draw!")
        return 0
    
    print("Testing Defender army.")
    if not validate_army(_def_army):
        print("Invalid army, resolving to Draw!")
        return 0
    

    max_army = max(len(_def_army), len(_att_army))
    print(f"Handling battle, longest army is {max_army} rows.")
    
    while len(_def_army) < len(_att_army):
        _def_army.append([0,0,0,0,0])

    while len(_def_army) > len(_att_army):
        _att_army.append([0,0,0,0,0])

    att_defeats = 0
    def_defeats = 0

    while att_defeats < max_army and def_defeats < max_army:

        att_line_defeats = 0
        def_line_defeats = 0

        for id in range(0,5):
            _curr_att = _att_army[att_defeats]
            _curr_def = _def_army[def_defeats]

            if _curr_att == [0,0,0,0,0] and _curr_def == [0,0,0,0,0]:
                att_defeats+=1
                def_defeats+=1
                break

            if _curr_att[id] > 9:
                print(f"Found invalid soldier count {_curr_att[id]}! Disqualifying Attacker!")
                att_defeats = max_army
                break

            if _curr_def[id] > 9:
                print(f"Found invalid soldier count {_curr_def[id]}! Disqualifying Defender!")
                def_defeats = max_army
                break

            #skip none-operations
            if _curr_att[id] == 0 and _curr_def[id] == 0:
                print(f"No living soldiers {_curr_att} vs {_curr_def}, skipping column {id+1}.")
                continue

            #attacker attack 
            # straight
            _curr_def[id] = do_attack(_curr_att[id], _curr_def[id])
            # left
            if id > 0:
                _curr_def[id-1] = do_attack(_curr_att[id], _curr_def[id-1])
            # right
            if id < 4:
                _curr_def[id+1] = do_attack(_curr_att[id], _curr_def[id+1])

            if _curr_def[id] == 0:
                def_line_defeats+=1

            #defender retaliation
            # straight
            _curr_att[id] = do_attack(_curr_def[id], _curr_att[id])
            # left
            if id > 0:
                _curr_att[id-1] = do_attack(_curr_def[id], _curr_att[id-1])
            # right
            if id < 4:
                _curr_att[id+1] = do_attack(_curr_def[id], _curr_att[id+1])

            if _curr_att[id] == 0:
                att_line_defeats+=1


            #check for defeat attacker side at end of line
            if att_line_defeats > def_line_defeats and id == 4 and _curr_att == [0,0,0,0,0]:
                att_defeats+=1

            #check for defeat defender side at end of line
            if def_line_defeats > att_line_defeats and id == 4 and _curr_def == [0,0,0,0,0]:
                def_defeats+=1

            #if we have suffered equal defeats on both these should be equal
            if def_line_defeats == att_line_defeats and id == 4 and _curr_def == [0,0,0,0,0] and _curr_att == [0,0,0,0,0]:
                def_defeats+=1
                att_defeats+=1

            # sort lines to force concflict if we end up unresolved
            if _curr_def != [0,0,0,0,0] and _curr_att != [0,0,0,0,0] and id == 4:
                _curr_def.sort()
                _curr_att.sort()

    if def_defeats > att_defeats:
        print(f"Attacker Victory! {att_defeats} defeats vs {def_defeats} defeats!")
        return 1
    if att_defeats > def_defeats:
        print(f"Attacker Defeat! {def_defeats} defeats vs {att_defeats} defeats!")
        return -1
    
    print("Draw! Nobody wins!")
    return 0

army1 = [[1,1,1,1,1],[0,0,1,0,0]]
army2 = [[2,0,1,0,2],[0,0,2,0,0]]
army3 = [[9,9,9,9,9]]
for i in range(99):
    army3.append([int(i/10),int(i/10),int(i/10),int(i/10),int(i/10)])
army4 = [[9,9,9,9,9]]
for i in range(75):
    army4.append([9,9,9,9,9])

res = resolve_fight(army1, army2) #1
print(res == 1)
res = resolve_fight(army3, army4) #1
print(res == 1)
res = resolve_fight(army1, [[9,9,9,9,9]]) #-1
print(res == -1)
res = resolve_fight([[0,0,0,0,0]], [[0,0,0,0,0]]) #0
print(res == 0)
res = resolve_fight([[0,0,9959,0,0]], [[0,0,0,0,0]]) #-1 (for cheated soldier count)
print(res == -1)
res = resolve_fight([[0,0,0,0,0]], [[0,0,901,0,0]]) #1 (for cheated soldier count)
print(res == 1)
res = resolve_fight([],[]) #0 (invalid inputs)
print(res == 0)
res = resolve_fight([1,2,3,2,1],[]) #0 (invalid inputs)
print(res == 0)
res = resolve_fight([[1,2,3,2,1],1],[]) #0 (invalid inputs)
print(res == 0)
res = resolve_fight([[1,0,0,0,0]],[[0,0,0,0,1]]) #1
print(res == 1)