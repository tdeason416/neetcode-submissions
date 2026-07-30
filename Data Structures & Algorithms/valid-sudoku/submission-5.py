class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_cells = {'1','2','3','4','5','6','7','8','9'}
        rows = {idx:{} for idx in range(10)}
        cols = {idx:{} for idx in range(10)}
        grps = {idx:{} for idx in range(10)}
        # row = 0
        col = 0
        grp = 3
        for row, rowarr in enumerate(board):
            col = 0
            grp -= 3
            if row != 0 and row % 3 == 0:
                grp += 3
            for cell in rowarr:
                if cell in valid_cells:
                    if rows[row].get(cell, None):
                        print('failed rows', row, col, grp, cell)
                        return False
                    elif cols[col].get(cell, None):
                        print('failed cols', row, col, grp, cell)
                        return False
                    elif grps[grp].get(cell, None):
                        for k,v in grps.items():
                            print(k,v)
                        print('failed grps', row, col, grp, cell)
                        return False
                    else:
                        rows[row][cell] = 1
                        cols[col][cell] = 1
                        grps[grp][cell] = 1
                col += 1
                if col % 3 == 0:
                    grp += 1
        return True


                


        