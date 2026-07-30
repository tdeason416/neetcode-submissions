class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        hts = heights
        wdth = len(hts) - 1
        p0 = 0
        p1 = len(hts) - 1
        while p1 > p0:
            print(p0,p1)
            h0 = hts[p0]
            h1 = hts[p1]
            min_ht = min(h1, h0)
            vol = min_ht * wdth
            if vol > max_vol:
                max_vol = vol
            if h1 >= h0:
                p0 += 1
            elif h1 < h0:
                p1 -= 1
            wdth -= 1
        return max_vol
            
                    
            






            # if h1 < h2:
            #     p1 += 1
            # elif h2 > h1:
            #     p2 -= 1
            # if h1 == h2:
            #     truncd = hts[p1+1:p2]
            #     for idx, val in enumerate(hts):
            #         if val > h1:
                        




        