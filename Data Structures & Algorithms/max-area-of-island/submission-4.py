class Solution:
    def __init___(self):
        self.island_idx = 1
        self.largest = 0
        self.ridx = 0
        self.cidx = 0
        self.grid = None
        self.largest = 0
        self.islands = dict()
        self.cells = dict()

    def add_to_island(self):
        ilen = 0
        left_id = None
        top_id = None
        # check left row for existing island
        if self.cells.get((self.ridx-1, self.cidx), -1) != -1:
            # get island_id
            left_id = self.cells[(self.ridx-1, self.cidx)]
            # print(f"adding {(self.ridx, self.cidx)} to left island {left_id}")
            ilen += len(self.islands[left_id])

        # check above row for existing island
        if self.cells.get((self.ridx, self.cidx - 1), -1) != -1:
            top_id = self.cells[(self.ridx, self.cidx-1)]
            # print(f"adding {(self.ridx, self.cidx)} to above island {top_id}")
            if top_id != left_id:
                ilen += len(self.islands[top_id])
            # if there was also an island to the left, rename the top island as left island
                if left_id:
                    for cell in self.islands[top_id]:
                        self.cells[cell] = left_id
                        self.islands[left_id].append(cell)
                        top_id = left_id

        if left_id:
            island = left_id
        elif top_id:
            island = top_id
        else:
            # create new island
            island = self.island_idx + 1
            self.island_idx += 1
            self.islands[island] = []


        self.cells[(self.ridx, self.cidx)] = island
        self.islands[island].append((self.ridx, self.cidx))

        if ilen + 1 > self.largest:
            self.largest = ilen + 1
        

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.island_idx = 1
        self.largest = 0
        self.ridx = 0
        self.cidx = 0
        # self.grid = None
        self.largest = 0
        self.islands = dict()
        self.cells = dict()
        self.grid = grid

        num_islands = 0
        self.prevrow = None
        for row in grid:
            self.prevcol = None
            for col in row:
                if col == 1:
                    self.add_to_island()
                self.cidx += 1
            self.cidx = 0
            self.ridx += 1

        return self.largest
                    


        