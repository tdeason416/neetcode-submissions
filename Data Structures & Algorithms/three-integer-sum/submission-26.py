class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        numlen = len(nums)
        n = sorted(nums)
        for p0 in range(1,len(nums)-1):
            nt = [x for x in n]
            v0 = nt.pop(p0)
            p1 = 0
            p2 = len(nt) - 1
            while nt[p1] <= v0  <= nt[p2]:
                v1 = nt[p1]
                v2 = nt[p2]
                intouts = [v1, v0, v2]
                r = sum(intouts)
                if r == 0:
                    if intouts not in results:
                        results.append(intouts)
                    p1 += 1
                    p2 -=1
                elif r < 0:
                    p1 += 1
                elif r > 0:
                    p2 -= 1
                if p1 >= p2:
                    break
        return sorted(results)

