class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        outputs = {}
        putouts = {}
        for i in nums:
            if i in outputs:
                outputs[i] += 1
                if outputs[i]+1 in putouts:
                    putouts[outputs[i]+1].append(i)
                else:
                    putouts[outputs[i] + 1] = [i]
            else:
                outputs[i] = 1
                putouts[1] = putouts.get(1,[]) + [i]
        deliv = set()
        while len(deliv) < k:
            for x in putouts[max(putouts)]:
                deliv.add(x)
            putouts.pop(max(putouts))
        return list(deliv)

        