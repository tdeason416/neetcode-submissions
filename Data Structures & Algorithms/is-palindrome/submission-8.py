class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = -1
        half = int(len(s) / 2 - .5)
        neghalf = (half + 1) * -1
        while True:
            if p1 >= len(s):
                return True
            if p1 > half and p2 < neghalf:
                return True
            elif not s[p1].isalnum():
                p1 += 1
            elif not s[p2].isalnum():
                p2 -= 1
            elif s[p1].lower() != s[p2].lower():
                return False
            else:
                p1 += 1
                p2 -= 1
        