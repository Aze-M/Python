nums1 = [2,7,11,15]
target1 = 9

nums2 = [3,2,4]
target2 = 6

nums3 = [3,3]
target3 = 6

def find_two_sum(list_numbers, int_target) -> list:

    number_buffer = {}

    for id,number in enumerate(list_numbers):
        complement = int_target - number

        if complement in number_buffer:
            return [number_buffer[complement], id]
        
        number_buffer[number] = id

            
print(find_two_sum(nums1,target1))
print(find_two_sum(nums2,target2))
print(find_two_sum(nums3,target3))