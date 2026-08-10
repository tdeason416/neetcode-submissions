from collections import Counter

class Solution:
    def isValid(self, s: str) -> bool:
        openfirst = {'(':')', '{':'}', '[':']'}
        nextval = []
        for c in s:
            if c in openfirst:
                nextval.append(openfirst[c])
            else:
                if len(nextval) == 0 or nextval.pop() != c:
                    return False
        if len(nextval) > 0:
            return False
        return True

        