class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        end = k
        window = nums[:k]
        vmax = float('-inf')
        imax = None
        def find_max(imax, vmax, window):
            for i, x in enumerate(window):
                if x > vmax:
                    imax = i
                    vmax = x
            return imax, vmax
        imax, vmax = find_max(imax, vmax, window)
        output = [vmax]
        for v in nums[k:]:
            window.append(v)
            window.pop(0)
            if v > vmax:
                vmax = v
                imax = k-1
            else:
                if imax == 0:
                    vmax = float('-inf')
                    imax, vmax = find_max(imax, vmax, window)
                else:
                    imax -= 1
            output.append(vmax)
        return output


        