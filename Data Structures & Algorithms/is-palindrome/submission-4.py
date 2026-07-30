class Solution:
    def isPalindrome(self, s: str) -> bool:
        # nospace = ''.join(s.split()).lower()
        nospace = ''.join(x for x in s if x.isalnum()).lower()
        for idx in range(int(len(nospace) / 2)):
            if nospace[idx] != nospace[-(idx + 1)]:
                return False
        return True
        