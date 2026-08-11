class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        numsort = sorted(nums, reverse=True)
        if len(nums) > k:
            numsort = numsort[:k]
        self.nums = {k+1:v for k,v in enumerate(numsort)}


    def add(self, val: int) -> int:
        rank = self.k
        print(self.nums)
        print(f"add {val}")
        while rank >= 1:
            if val < self.nums.get(rank, -float('infinity')):
                print(val, self.nums.get(rank, -float('infinity')))
                print(list(range(self.k-1, rank, -1)))
                for tk in range(self.k-1, rank, -1):
                    self.nums[tk + 1] = self.nums.get(tk, -float('infinity'))
                if rank +1 <= self.k:
                    self.nums[rank + 1] = val
                return self.nums[self.k]
            rank -= 1

        #rebuild the whole dictionary
        for tk in range(self.k-1, 0, -1):
            self.nums[tk + 1] = self.nums.get(tk, -float('infinity'))    
        self.nums[1] = val
        return self.nums[self.k]
            


        
