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
            print(idx, v.cur_height, h, total_volume, v.partial_volume)

            # cache partial container without resetting values
            # if h < v.cur_height:
            #     partial_volume = v.volume - (v.width - 1) * (v.max_height - v.cur_height)
            #     print(f'volume: {v.volume}, max_height: {v.max_height} last_height: {v.cur_height}, width {v.width - 1}, total: {partial_volume}')
            #     # v.partial_volume = v.volume - v.width * (v.max_height - h)
            #     if partial_volume > v.partial_volume:
            #         v.partial_volume = partial_volume


            if h > v.cur_height:
                partial_vol = 0
                for h_min in v.prev_mins:
                    pv0 = h - h_min
                    if pv0 > 0:
                        partial_vol += pv0
                if partial_vol > v.partial_volume:
                    v.partial_volume = partial_vol
                # # partial_volume = v.volume - (v.width) * (v.max_height - v.cur_height)
                # partial_volume = v.volume - (v.width) * (v.max_height - h)
                # print(f'volume: {v.volume}, max_height: {v.max_height} last_height: {h}, width {v.width}, total: {partial_volume}')
                # # v.partial_volume = v.volume - v.width * (v.max_height - h)
                # if partial_volume > v.partial_volume:
                #     v.partial_volume = partial_volume

            v.width += 1

            # check for container end state
            if h >= v.max_height:
                # print('idx:', idx, 'height:', h, 'volume:', v.volume)
                total_volume += v.volume
                # start_the container
                print('new vessel')
                v = Vessel()
                v.max_height = h

            # add volume
            v.volume += abs(v.max_height - h)
            v.prev_mins.append(h)
            # v.width += 1
            # print(f"added {abs(v.max_height - h)} at {idx}.  Volume is now {v.volume}")
            v.cur_height = h
            # print(total_volume)

        # add partial container if exists
        total_volume += v.partial_volume
        return total_volume
