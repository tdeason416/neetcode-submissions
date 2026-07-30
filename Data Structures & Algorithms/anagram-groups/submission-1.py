class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputs = {}
        for s in strs:
            baseset = ''.join(sorted(s))
            if baseset in outputs:
                outputs[baseset].append(s)
            else:
                outputs[baseset] = [s]
        return [v for v in outputs.values()]

        