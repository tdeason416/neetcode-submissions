class Vessel(object):
    def __init__(self):
        self.max_height = 0
        self.cur_height = 0
        self.width = 0
        self.volume = 0
        self.partial_volume = 0 
        self.prev_mins = []

class Solution:
    def trap(self, height: List[int]) -> int:
        largest_container = 0
        total_volume = 0
        local_max = 0
        v = Vessel()
        for idx, h in enumerate(height):
            # cache partial container without resetting values
            if h > v.cur_height:
                partial_vol = 0
                for h_min in v.prev_mins:
                    pv0 = h - h_min
                    if pv0 > 0:
                        partial_vol += pv0
                if partial_vol > v.partial_volume:
                    v.partial_volume = partial_vol


            # check for container end state
            if h >= v.max_height:
                total_volume += v.volume
                # start_the container
                v = Vessel()
                v.max_height = h

            # add volume to cell
            v.volume += abs(v.max_height - h)
            v.prev_mins.append(h)
            v.width += 1
            v.cur_height = h

        # add partial container if exists
        total_volume += v.partial_volume
        return total_volume
