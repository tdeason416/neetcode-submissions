class Solution:
    def search(self, nums: List[int], target: int) -> int:

        idx = int(len(nums) / 2 - 0.5)
        idx_global = idx
        val = nums[idx]

        while val != target:
            if target > val:
                nums = nums[idx+1:]
                idx = int(len(nums) / 2 - 0.5)
                idx_global = idx_global + idx + 1
            elif target < val:
                nums = nums[:idx]
                idx = int(len(nums) / 2 - 0.5)
                idx_global = idx_global - len(nums) + idx
            if len(nums) == 0:
                return -1
            val = nums[idx]

        return idx_global



        