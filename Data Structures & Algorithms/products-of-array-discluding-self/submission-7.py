def dumb_math(lst):
    x = 1
    while True:
        n = lst.pop(0)
        x *= n
        if len(lst) == 0:
            return x


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = []
        for idx in range(len(nums)):
            solution.append(dumb_math(nums[:idx] + nums[idx+1:]))
        return solution
    

        