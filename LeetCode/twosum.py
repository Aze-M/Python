nums1 = [2,7,11,15]
target1 = 9

nums2 = [3,2,4]
target2 = 6

nums3 = [3,3]
target3 = 6

def find_two_sum(list_numbers, int_target) -> str:

    number_buffer = []

    for id,number in enumerate(list_numbers):
        number_buffer.append((number,id))

        for buffered_number in number_buffer:
            if number + buffered_number[0] == int_target and buffered_number[1] != id:
                return f"({buffered_number[1]} , {id})"
            
print(find_two_sum(nums1,target1))
print(find_two_sum(nums2,target2))
print(find_two_sum(nums3,target3))