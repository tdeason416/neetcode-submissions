from collections import Counter

class Solution:
    def isValid(self, s: str) -> bool:
        openfirst = {'(':')', '{':'}', '[':']'}
        nextval = []
        for c in s:
            if c in openfirst:
                nextval.append(openfirst[c])
                print(f"added '{openfirst[c]}' to nextval")
            else:
                if len(nextval) == 0 or nextval.pop() != c:
                    print(f"Error: '{c}' not in nextval")
                    return False
                print(f"removed '{c}' from nextval")
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

        