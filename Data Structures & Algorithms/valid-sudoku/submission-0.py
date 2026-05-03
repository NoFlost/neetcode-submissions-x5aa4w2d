class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = [[] for _ in range(9)]
        columns = [["0"] * 9 for _ in range(9)]
        rows = board
        
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val != ".":
                    columns[j][i] = val
                    squares[int(i/3)*3 + int(j/3)].append(val)
        
        if self.containsDuplicate(squares) == True:
            return False
        if self.containsDuplicate(rows) == True:
            return False
        if self.containsDuplicate(columns) == True:
            return False

        return True

    def containsDuplicate(self, nums: List[List[str]]) -> bool:
        
        for i, row in enumerate(nums):
            set_ = set()
            for j, val in enumerate(row):
                if val != "." and val != "0":
                    if val in set_:
                        return True
                    set_.add(val)
        
        return False