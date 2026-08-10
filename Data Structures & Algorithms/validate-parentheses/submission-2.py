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




        # must_have = Counter()
        # openfirst = {'(':')', '{':'}', '[':']'}
        # closes = set(openfirst.values())
        # # closefirst = {v:k for k,v in openfirst.items()}
        # for c in s:
        #     if c in openfirst:
        #         # add a counter to the bracket closes
        #         must_have[openfirst[c]] += 1
        #     elif c in closes:
        #         # if close before open, return False
        #         if c not in must_have:
        #             return False
        #         # remove value from bracket closes
        #         must_have[c] -= 1
        #         if must_have[c] == 0:
        #             must_have.pop(c)
        # if must_have:
        #     return False
        # return True

        