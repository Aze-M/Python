import time

starttime = time.perf_counter()

nums1 = [2,7,11,15]
target1 = 9

nums2 = [3,2,4]
target2 = 6

nums3 = [3,3]
target3 = 6

def find_two_sum(list_numbers, int_target) -> list:
    list_answer = []

    #Hier könnte dein code stehen!

    return list_answer
            
print(find_two_sum(nums1,target1))
print(find_two_sum(nums2,target2))
print(find_two_sum(nums3,target3))

print(f"Total time {(time.perf_counter() - starttime)*1000:0.0f}ms")