""" SUDOKU SOLVER

Row checks then column checks, then box checks
"""
from math import ceil

class Sudoku(object):
    def __init__(self):
        self.box = []
        for x in range(9):
            self.box.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
            
    def __repr__(self):
        reprstr = " --------------------\n"
        for a in range(9):
            for b in range(3):
                reprstr += "|"
                for c in range(3):
                    reprstr += " "
                    if self.box[a][(3*b)+c] == 0:
                        reprstr += "."
                    else:
                        reprstr += str(self.box[a][(3*b)+c])
            if a % 3 == 2:
                reprstr += "|\n --------------------\n"
            else:
                reprstr += "|\n"
        return reprstr

    def GetCol(self, col): #list of single column
        colList = []
        for row in self.box:
            colList.append(row[col-1])
        return colList

    def GetBox(self, box_num): #3 lists of 3 items
        YSTARTS = (0, 0, 0, 3, 3, 3, 6, 6, 6)
        result = []
        StartX = ((box_num % 3) - 1)* 3
        StartY = YSTARTS[box_num - 1]
        result.append(self.box[StartY][StartX: StartX + 3])
        result.append(self.box[StartY+ 1][StartX: StartX + 3])
        result.append(self.box[StartY+ 2][StartX: StartX + 3])
        return result
    
    def InRow(self, num, row_num): # is num in this row?
        if num in self.box[row_num - 1]:
            return True
        else:
            return False

    def InCol(self, num, col_num): # is num in this column?
        for x in range(9):
            if num == self.box[x][col_num - 1]:
                return True
        return False

    def InBox(self, num, box_num): #boxes numbered left to right, top to bottom
        x = ((box_num - 1) % 3)* 3
        if box_num <=3:
            y = 0
        elif box_num <= 6:
            y = 3
        else:
            y = 6
        this_box = self.box[y][x:x+3] + self.box[y+1][x:x+3] + self.box[y+2][x:x+3]
        if num in this_box:
            return True
        else:
            return False

    def Fill(self): #manually fill sudoku
        for x in range(9):
            row = input("Enter row>>")
            for y in range(9):
                self.box[x][y] = int(row[y])
        
S = Sudoku()

def CheckRow(Sud, num, rownum):
    #try to solve for one num in one row
    row = Sud.box[rownum-1][:]
    if num in row:
        return row
    BoxX = (1, 1, 1, 2, 2, 2, 3, 3, 3)
    BoxY = (0, 0, 0, 3, 3, 3, 6, 6, 6)
    
    for x in range(9):
        if row[x] == 0:
            if Sud.InCol(num, x + 1):
                row[x] = -1
            if Sud.InBox(num, (BoxX[x] + BoxY[rownum-1])):
                row[x] = -1
                
    if row.count(0) == 1:   #only one spot left for num
        row[row.index(0)] = num    

    for x in range(9):  #remove -1 placeholders
        if row[x] == -1:
            row[x] = 0
            
    return row

def CheckCol(Sud, num, colnum):
    #try to solve for one num in one col
    col = Sud.GetCol(colnum)
    if num in col:
        return col
    BoxX = (1, 1, 1, 2, 2, 2, 3, 3, 3)
    BoxY = (0, 0, 0, 3, 3, 3, 6, 6, 6)
    
    for y in range(9):
        if col[y] == 0:
            if Sud.InRow(num, y + 1):
                col[y] = -1  
            if Sud.InBox(num, (BoxX[colnum-1] + BoxY[y])):
                col[y] = -1
                
    if col.count(0) == 1:   #only one spot left for num
        col[col.index(0)] = num    

    for x in range(9):  #remove -1 placeholders
        if col[x] == -1:
            col[x] = 0
            
    return col

def CheckBox(Sud, num, boxnum):
    pass
S.box = [[0, 0, 1, 0, 0, 0, 9, 8, 0],
         [0, 0, 0, 1, 3, 8, 0, 0, 0],
         [6, 0, 8, 4, 0, 9, 1, 0, 7],
         [0, 5, 4, 0, 0, 0, 3, 6, 0],
         [0, 9, 0, 0, 0, 0, 0, 1, 0],
         [0, 8, 2, 0, 0, 0, 4, 7, 0],
         [8, 0, 0, 7, 0, 1, 0, 0, 2],
         [0, 0, 0, 5, 8, 2, 7, 0, 0],
         [0, 0, 5, 0, 0, 0, 8, 0, 0]] #pg 106


def Solve(Sudoku):
    
    for b in range(20):
        for x in range(9): #test all rows first
            for z in range(9):
                Sudoku.box[x] = CheckRow(Sudoku, z + 1, x + 1)
        for y in range(9): #test all cols 
            for z in range(9):
                newcol = CheckCol(Sudoku, z + 1, y + 1)
                for row in range(9):
                    Sudoku.box[row][y] = newcol[row]
                    
    print(S)



        
