class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        numlen = len(nums)
        n = sorted(nums)
        print(n)
        for p0 in range(1,len(nums)-1):
            nt = [x for x in n]
            v0 = nt.pop(p0)
            # print("\n\nstatic_index:", p0, "Value:", v0)
            # print(nt)
            p1 = 0
            p2 = len(nt) - 1
            while nt[p1] <= v0  <= nt[p2]:
            # for x in range(15):
                # if nt[p1] <= v0  <= nt[p2]:
                    # break
                v1 = nt[p1]
                v2 = nt[p2]
                intouts = [v1, v0, v2]
                r = sum(intouts)
                if r == 0:
                    if intouts not in results:
                        # print("added:", intouts, "to results, sum:", r)
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

