class Solution:

    def is_between(self, lst, mindex, maxdex, target):
        if lst[mindex] < lst[maxdex]:
            if lst[maxdex] > target and lst[mindex] < target:
                return True
            return False
        elif lst[mindex] > lst[maxdex]:
            if lst[mindex] > target and lst[maxdex] < target:
                return False
            return True


    def search(self, nums: List[int], target: int) -> int:
        o_len = len(nums)
        idx_base = 0
        while True:
            # print(idx_base, len(nums), nums)
            if nums[0] == target:
                return idx_base
            if nums[-1] == target:
                return idx_base + len(nums) - 1
            if len(nums) <= 2:
                return -1
            halfnums = int(len(nums) / 2)
            result = self.is_between(nums, 0, halfnums, target)

            if result:
                nums = nums[:halfnums+1]
            else:
                nums = nums[halfnums:]
                idx_base += halfnums

        