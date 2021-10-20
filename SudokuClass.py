# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 01:56:24 2020

@author: Dafydd
"""

import numpy as np
class sudoku:
    def __init__(self, file):
        sudoku = []
        with open(file, 'r')as base_file:
            for l in base_file:
                if not ("+" in l):
                    reading = list("".join(l.split("|")))[0:9]
                    row = [int(x) for x in reading]
                    sudoku.append(row)
        self.puzzle = sudoku
                    
    def get_box(self,row,col):
        row +=-1
        col +=-1
        value = self.puzzle[row][col]
        return value
    
    def set_box(self, row, col, value):
        row += -1
        col += -1
        self.puzzle[row][col] = value
        return
        
    def get_row(self, row):
        values = []
        for i in range(1,10):
            v = self.get_box(row,i)
            values.append(v)
        return values
    
    def get_column(self, column):
        values = []
        for i in range(1,10):
            v = self.get_box(i,column)
            values.append(v)
        return values
    
    def get_bigbox(self, row, column):
        
        if row in range(1,4):
            big_row = 1
            rows = range(1,4)
        elif row in range(4,7):
            big_row = 2
            rows = range(4,7)
        elif row in range (7,10):
            big_row = 3
            rows = range(7,10)
        if column in range(1,4):
            big_column = 1
            columns = range(1,4)
        elif column in range(4,7):
            big_column = 2
            columns = range(4,7)
        elif column in range (7,10):
            big_column = 3
            columns = range(7,10)
        values = []
        for r in rows:
            for c in columns:
                values.append(self.get_box(r,c))
        return values
    
    def is_solved(self):
        solve = True
        for i in range(1,10):
            if 0 in self.get_row(i):
                solve = False
                break
        
        return solve
    
    def find_missing(self, values):
        possibs = np.array(range(1,10))
        truth_array = np.zeros(9, dtype=int)
        for x in values:
            if x in possibs:
                truth_array[x-1] = 1
        out = -1*truth_array + 1
        return out
    
    def find_poss(self, row, column):
        if self.get_box(row, column) != 0:
            return self.get_box(row, column)
        values_b = self.get_bigbox(row, column)
        values_r = self.get_row(row)
        values_c = self.get_column(column)
        
        t_array_b = self.find_missing(values_b)
        t_array_r = self.find_missing(values_r)
        t_array_c = self.find_missing(values_c)
        
        t_array_all = t_array_b*t_array_r*t_array_c
        missing = t_array_all*np.array(range(1,10))
        poss = [x for x in missing if x != 0]
        
        return poss
    
    def print_sudoku(self, file):
        with open(file, 'w') as out_file:
            for i in range(1,10):
                row = self.get_row(i)
                if i != 1:
                    out_file.write("\n")
                p1 = "".join([str(x) for x in row[0:3]])
                p2 = "".join([str(x) for x in row[3:6]])
                p3 = "".join([str(x) for x in row[6:9]])
                line = "|".join([p1,p2,p3])
                out_file.write(line)
                if (i in [3,6]):
                    out_file.write("\n---+---+---")
    
    def solve(self):
        solved = self.is_solved()
        i = 0
        while not solved:
            #print(str(i)+" loop")
            for r in range(1,10):
                for c in range(1,10):
                    poss = self.find_poss(r,c)
                    if type(poss) != list:
                        pass
                    elif(len(poss) == 1):
                        self.set_box(r, c, poss[0])
                    else:
                        pass
            i += 1
            solved = self.is_solved()
            if i > 10:
                break
        print("Sudoku solved")
        return
        