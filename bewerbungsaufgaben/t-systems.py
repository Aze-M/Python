def get_target_from_arrays(_in_arr1: list, _in_arr2: list, _target: int) -> bool:
    _dict_arr2 = {}

    for number in _in_arr2:
        if number not in _dict_arr2.keys():
            _dict_arr2[number] = True
        
    for number in _in_arr1:
        remainder = _target - number

        if remainder in _dict_arr2.keys():
            print(f"{number} + {remainder} = {target}")
            return True
        
    return False

arr1 = [1,2,3,4]
arr2 = [-1,2,-3,4]

target = int(input("Input tager number to get from [1,2,3,4] and [-1,2,-3,4]: "))

print(get_target_from_arrays(arr1,arr2,target))
