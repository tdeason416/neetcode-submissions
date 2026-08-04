from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        strs = Counter()
        wndw = Counter()
        for i in s1:
            strs[i] += 1
        idx0 = 0
        for idx in range(len(s2)):
            # check if wndw contains enough values
            if idx - idx0 == len(s1):
                # if so, drop lowest index
                wndw[s2[idx0]] -= 1
                if wndw[s2[idx0]] == 0:
                    wndw.pop(s2[idx0])
                idx0 += 1
            # add new value to wndw
            wndw[s2[idx]] += 1
            # check if match
            if strs == wndw:
                return True
        # if no match, return False
        return False


      