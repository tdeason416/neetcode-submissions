from math import ceil

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # while True:
        minval = nums[0]
        idx1 = len(nums) // 2
        idx0 = 0
        # while True:
        for i in range(100):
            r0 = nums[idx0]
            r1 = nums[idx1]
            print(idx0, idx1)
            print("\t", r0, r1)
            if idx0 == idx1:
                return minval
            if r0 > r1:
                if idx1 - idx0 == 1:
                    return r1
                idx1 -= (idx1 - idx0) // 2
            elif r0 < r1:
                if idx1 == len(nums) - 1:
                    return nums[0]
                d = ceil((idx1 - idx0) / 2)
                idx0 = idx1
                idx1 += d
                if idx1 >= len(nums) - 1:
                    idx1 = len(nums) - 1
                


