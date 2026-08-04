from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # # debugging
        # row_num = 0
        # #
        let_counts = Counter()
        max_count = 0
        cont_strs = {}
        replacements = Counter()
        for l in s:
            if l in let_counts:
                # add one
                let_counts[l] += 1
                cont_strs[l] += l
            else:
                ## add to replacements
                let_counts[l] = k + 1
                cont_strs[l] = l
                replacements[l] = k
            # print(l, let_counts, replacements, cont_strs)
            for x in list(let_counts.keys()):
                if x != l:
                    if replacements[x] > 0:
                        cont_strs[x] += l
                        replacements[x] -= 1
                    else:
                        if let_counts[x] > max_count:
                            max_count = let_counts[x]
                        for idx, char in enumerate(cont_strs[x]):
                            if char != x:
                                cont_strs[x] =  cont_strs[x][idx+1:] + l
                                break
                            else:
                                let_counts[x] -= 1
                        if let_counts[x] <= k:
                            replacements.pop(x)
                            let_counts.pop(x)
                            cont_strs.pop(x)
            # # debugging
            # row_num += 1
            # #
        for v in let_counts.values():
            if v > max_count:
                max_count = v
        if max_count < len(s):
            return max_count
        return len(s)

         