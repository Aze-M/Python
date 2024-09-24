class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(m, n+m):
            nums1[i] = nums2[i-m]
        
        nums1.sort()

n1 = [1,2,3,0,0,0]
m = 3
n2 = [2,5,6]
n = 3

Solution.merge(Solution,n1,m,n2,n)

print(n1)

