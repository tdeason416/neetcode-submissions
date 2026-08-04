class Solution:
    def __init__(self):
        self.idx_min = 0
        self.lets = ''
        self.length = 0
        self.loc_global = {}
        self.longest = 0

    def lengthOfLongestSubstring(self, s: str) -> int:
        for idx, l in enumerate(s):
            if l in self.loc_global:
                if self.length > self.longest:
                    self.longest = self.length
                new_min = self.loc_global[l] + 1
                new_str = self.lets[self.loc_global[l] + 1:idx]
                for l0, i in enumerate(s[self.idx_min: self.loc_global[l] + 1]):
                    self.loc_global.pop(i)
                    self.length -= 1
                self.idx_min = new_min
                self.lets = new_str
            self.lets += l
            self.loc_global[l] = idx
            self.length += 1
            # print('cur_let:',l, 'cur_string:',self.lets, 'cur_dict', self.loc_global, 'str_start:',self.idx_min, 'len:', self.length)
        if self.length > self.longest:
            self.longest = self.length
        return self.longest

