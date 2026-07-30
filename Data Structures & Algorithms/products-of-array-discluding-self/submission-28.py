from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solutions = [1 for i in nums]
        # endprod = 1
        # stprod = 1

        h_idx = int(len(nums) / 2 + .5)
        stprod = prod(nums[:h_idx])
        endprod = prod(nums[h_idx+1:])
        i = 1
        # print(h_idx, nums[:h_idx-1], nums[h_idx:], endprod * stprod)
        # print(solutions, endprod, stprod, endprod*stprod)
        solutions[h_idx] = endprod * stprod
        # print(solutions, stprod, endprod, h_idx)
        while True:
            # print(solutions, stprod, endprod, i)
            if h_idx - i < 0:
                return solutions
            endprod *= nums[h_idx - i + 1]
            # print(endprod, prod(nums[:h_idx - i]))
            solutions[h_idx -i] *= endprod * prod(nums[:h_idx - i])
            if h_idx + i  < len(nums):
                stprod *= nums[h_idx + i - 1]
                solutions[h_idx + i] *= stprod * prod(nums[h_idx + i + 1:])
            # print(solutions, stprod, endprod, i)
            i += 1
            
            
        # return solutions




    

        