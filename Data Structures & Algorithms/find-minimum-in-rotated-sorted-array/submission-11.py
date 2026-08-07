from math import ceil

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # while True:
        minval = nums[0]
        maxval = 0
        for i in range(30):
            # print(len(nums))
            if len(nums) == 1:
                return minval
            idx0 = 0
            idx1 = ceil((len(nums)-1)/2)
            r0 = nums[idx0]
            r1 = nums[idx1]
            # print(idx0,idx1)
            # print("\t", r0,r1)

            if r0 > r1:
                if r0 > maxval:
                    maxval = r0
                if r1 < minval:
                    minval = r1
                nums = nums[:idx1]
                if idx1 - idx0 == 1:
                    return r1
            elif r0 < r1:
                if r0 < minval:
                    minval = r0
                nums = nums[idx1:]



