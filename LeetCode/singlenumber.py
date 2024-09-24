nums = [2,2,1]

def singleNumber(in_nums: list[int]) -> int:
    answer = 0

    for num in in_nums:
        answer ^= num

    return answer

ans1 = singleNumber(nums)

print(ans1)
