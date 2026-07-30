class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        numlen = len(nums)
        n = sorted(nums)
        print(n)
        for p0 in range(len(nums)-2):
            # nt = [x for x in n]
            # v0 = nt.pop(p0)
            v0 = n[p0]
            # print("\n\nindex:", p0, "value:", v0)
            if v0 > 0:
                break
            p1 = p0 + 1
            p2 = len(n) - 1
            # while nt[p1] <= v0  <= nt[p2]:
            while p1 < p2:
                v1 = n[p1]
                v2 = n[p2]
                intouts = [v0, v1, v2]
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
        return sorted(results)
                # if p1 >= p2:
                #     break
            
            # while nt[p1] <= v0  <= nt[p2]:
            #     v1 = nt[p1]
            #     v2 = nt[p2]
            #     intouts = [v1, v0, v2]
            #     r = sum(intouts)
            #     if r == 0:
            #         if intouts not in results:
            #             results.append(intouts)
            #         p1 += 1
            #         p2 -=1
            #     elif r < 0:
            #         p1 += 1
            #     elif r > 0:
            #         p2 -= 1
            #     if p1 >= p2:
            #         break
        # return sorted(results)

