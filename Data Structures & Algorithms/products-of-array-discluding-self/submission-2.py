import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = []
        for idx in range(len(nums)):
            solution.append(math.prod(nums[:idx] + nums[idx+1:]))
        return solution
        