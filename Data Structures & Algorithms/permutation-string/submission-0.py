from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        strs = Counter()
        wndw = Counter()
        for i in s1:
            strs[i] += 1
        idx0 = 0
        for idx in range(len(s2)):
            #drop lowest value
            if idx - idx0 == len(s1):
                wndw[s2[idx0]] -= 1
                if wndw[s2[idx0]] == 0:
                    wndw.pop(s2[idx0])
                idx0 += 1

            # print(idx0, idx, wndw)
            # add new value
            wndw[s2[idx]] += 1
            # check if match
            if strs == wndw:
                return True
        
        return False


      