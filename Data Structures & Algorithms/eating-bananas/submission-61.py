from math import ceil

def measure_speed(piles, k):
    time_taken = 0
    for pile in piles:
        t_cell = ceil(pile / k)
        time_taken += t_cell
    return time_taken

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        plen = len(piles)

        # if plen == 1:
        #     return int(piles[0] / h + .01)

        # sort them
        ord_piles = sorted(piles)
        idx = int(len(ord_piles) / 2 - .5)

        # k-max each cell is the same size as the largest cell
        # k_max = ceil(ord_piles[-1] / (h / plen))
        k_max = ord_piles[-1]

        # k-min each cell is the same size as the smallest cell
        # k_min = int(ord_piles[0] / (h / plen))
        k_min = ord_piles[0]

        # k = int((k_max - k_min) / 2) + 1
        # k = k_min + ceil((k_max - k_min) / 2)
        k = k_max
        delta = int(k / 2)


        print(k_min, k_max, k, delta, ord_piles)
        ## find inital point
        time = measure_speed(ord_piles, k)
        # delta = k / 2

        print(f"inital values -- t:{time}, h:{h}, k:{k}, ord_piles:{ord_piles[:50]}")

        # while True:
        for _ in range(100):
            # print(k, time, h)
            if time > h:
                prev_k = k
                k = ceil(k + delta)
                delta = delta * .5
                time = measure_speed(ord_piles, k)
                # delta = ceil(delta - delta*(time - h) / h)
                print(f"increased k -- t:{time}, h:{h}, k:{k}, delta:{delta}")
            elif time <= h:
                if k == 1:
                    return k
                new_time = measure_speed(ord_piles, k-1)
                if new_time > h:
                    print(k-1, new_time - h)
                    return k
                prev_k = k
                k = int(k - delta)
                if k <= 0:
                    k = 1
                delta = delta * .5
                time = measure_speed(ord_piles, k)
                # delta = 1 + int(delta - delta*(time - h) / h)
                # delta = 1 + int(k - delta*(time - h) / h)
                print(f"decreased k -- t:{time}, h:{h}, k:{k}, delta:{delta}")






        