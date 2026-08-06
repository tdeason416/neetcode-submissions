from math import ceil

def measure_speed(piles, k, h):
    # remainders = []
    # cell_times = []
    time_float = 0
    time_taken = 0
    for pile in piles:
        t_cell = ceil(pile / k)
        time_float += pile / k
        # cell_times.append(t_cell)
        time_taken += t_cell
        # remainders.append(pile % k)
    # return time_taken, remainders, cell_times
    return time_taken, time_float / h, time_taken / h

def find_smallest_rem(remainders):
    rem = float('infinity')
    for i, r in enumerate(remainders):
        if r < rem:
            rem = r
    return rem

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        plen = len(piles)
        # rate_nominal = int(h / len(piles))

        # sort them
        ord_piles = sorted(piles)
        idx = int(len(ord_piles) / 2 - .5)

        ## assume the whole time is taken on the largest cell and move k down from there
        k = ceil(ord_piles[-1] / (h / plen))

        ## find inital point
        time, ratio, ratio_int = measure_speed(ord_piles, k, h)
        delta = k / 2

        while True:
            if time > h:
                prev_k = k
                k = ceil(k + delta)
                delta = delta / 2
                time, ratio, ratio_int = measure_speed(ord_piles, k, h)
            elif time <= h:
                if k == 1:
                    return k
                new_time, _, _ = measure_speed(ord_piles, k-1, h)
                if new_time > h:
                    print(k-1, new_time - h)
                    return k
                # if k > 10:
                prev_k = k
                k = int(k - delta)
                delta = delta / 2
                time, ratio, ratio_int = measure_speed(ord_piles, k, h)






        