# def rec_chain_building(num, chains, end, pol)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # vals_needed = {}
        on_chain = set()
        starts = {}
        ends = {}
        chains = {}
        chain_no = 0
        max_len = 0
        for num in nums:
            while True:
                if num in on_chain:
                    break
                if num in starts and num in ends:
                    s_idx = starts.pop(num)
                    e_idx = ends.pop(num)
                    ends[chains[s_idx][-1] + 1] =  e_idx
                    chains[e_idx] = chains[e_idx] + [num] + chains[s_idx]
                    if len(chains[e_idx]) > max_len:
                        max_len = len(chains[e_idx])
                    on_chain.add(num)
                    break
                elif num in starts:
                    chain_idx = starts.pop(num)
                    chains[chain_idx] = [num] + chains[chain_idx]
                    starts[num - 1] = chain_idx
                    if len(chains[chain_idx]) > max_len:
                        max_len = len(chains[chain_idx])
                    on_chain.add(num)
                    num += 1
                elif num in ends:
                    chain_idx = ends.pop(num)
                    chains[chain_idx] = chains[chain_idx] + [num]
                    ends[num + 1] = chain_idx
                    if len(chains[chain_idx]) > max_len:
                        max_len = len(chains[chain_idx])
                    on_chain.add(num)
                    num -= 1
                else:
                    chain_no += 1
                    chains[chain_no] = [num]
                    starts[num - 1] = chain_no
                    ends[num + 1] = chain_no
                    if len(chains[chain_no]) > max_len:
                        max_len = len(chains[chain_no])
                    on_chain.add(num)
                    break
        return max_len

                
        