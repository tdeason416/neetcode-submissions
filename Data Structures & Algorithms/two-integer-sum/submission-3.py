class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for iloc, i in enumerate(nums):
            for jloc, j in enumerate(nums):
                if iloc == jloc:
                    continue
                elif i + j == target:
                    return [iloc, jloc]

        