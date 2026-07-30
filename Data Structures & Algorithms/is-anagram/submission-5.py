class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t = list(t)
        for i in s:
            if i not in t:
                return False
            t.remove(i)
        return True
            
        # return sorted(s) == sorted(t)

         