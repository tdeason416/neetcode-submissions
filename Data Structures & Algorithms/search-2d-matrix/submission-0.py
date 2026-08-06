def mat_to_linear(rows):
    new_mat = []
    for row in rows:
        new_mat += row
    return new_mat


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        linmat = mat_to_linear(matrix)
        idx = int(len(linmat) / 2 - .5)
        val = linmat[idx]
        if val == target:
            return True

        while val != target and len(linmat) > 0:
            if val < target:
                linmat = linmat[idx+1:]
            elif val > target:
                linmat = linmat[:idx]
            if len(linmat) == 0:
                return False
            idx = int(len(linmat) / 2)
            # print(matrix)
            # print(linmat)
            # print(idx)
            val = linmat[idx]
            if val == target:
                return True
        
        return False



        