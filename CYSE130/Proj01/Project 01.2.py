#!/usr/bin/env python
# coding: utf-8

# In[6]:


import xlrd
import xlwt
from xlwt import Workbook

#loc = r"C:\Users\harun\OneDrive\Documents\GMU\CYSE130\Proj01\CYST003.xls"

loc = input("Enter the file path of the CYST003 file: ")
loc2 = input("Enter the file path where you want to save the new/updated CYST003 file - Include the file name (*.xls): ")

wb = xlrd.open_workbook(r"{}".format(loc))
wbw = xlwt.Workbook()
sheet = wb.sheet_by_index(0)
sheetn = wbw.add_sheet('Extra_Credit Sheet')

name = [None] * (sheet.nrows - 1)
fname = [None] * (sheet.nrows - 1)
lname = [None] * (sheet.nrows - 1)
hw1 = [None] * (sheet.nrows - 1)
hw2 = [None] * (sheet.nrows - 1)
hw3 = [None] * (sheet.nrows - 1)
hw4 = [None] * (sheet.nrows - 1)
hw5 = [None] * (sheet.nrows - 1)
mid = [None] * (sheet.nrows - 1)
fnl = [None] * (sheet.nrows - 1)
hw = [None] * (sheet.nrows - 1)
agg = [None] * (sheet.nrows - 1)
letter = [None] * (sheet.nrows - 1)
#print(sheet.nrows)

for i in range(1, sheet.nrows):
    x = i - 1
    fname[x] = sheet.cell_value(i, 1)
    lname[x] = sheet.cell_value(i, 0)
    name[x] = fname[x] + ' ' + lname[x]
    hw1[x] = sheet.cell_value(i, 2)
    hw2[x] = sheet.cell_value(i, 3)
    hw3[x] = sheet.cell_value(i, 4)
    hw4[x] = sheet.cell_value(i, 5)
    hw5[x] = sheet.cell_value(i, 6)
    mid[x] = sheet.cell_value(i, 7)
    fnl[x] = sheet.cell_value(i, 8)

    hw[x] = (hw1[x] + hw2[x] + hw3[x] + hw4[x] + hw5[x])/5
    
    agg[x] = (0.6*hw[x]*10) + (0.2*mid[x]) + (0.2*fnl[x])
    
    if agg[x] >= 94:
        letter[x] = 'A'
    elif agg[x] >= 93:
        letter[x] = 'A-'
    elif agg[x] >= 89:
        letter[x] = 'B+'
    elif agg[x] >= 85:
        letter[x] = 'B'
    elif agg[x] >= 82:
        letter[x] = 'B-'
    elif agg[x] >= 79:
        letter[x] = 'C+'
    elif agg[x] >= 75:
        letter[x] = 'C'
    elif agg[x] >= 72:
        letter[x] = 'C-'
    elif agg[x] >= 69:
        letter[x] = 'D+'
    elif agg[x] >= 65:
        letter[x] = 'D'
    elif agg[x] >= 62:
        letter[x] = 'D-'
    else:
        letter[x] = 'F'

sheetn.write(0, 0, 'Last Name')
sheetn.write(0, 1, 'First Name')
sheetn.write(0, 2, 'Hw1 (out of 10)')
sheetn.write(0, 3, 'Hw2 (out of 10)')
sheetn.write(0, 4, 'Hw3 (out of 10)')
sheetn.write(0, 5, 'Hw4 (out of 10)')
sheetn.write(0, 6, 'Hw5 (out of 10)')
sheetn.write(0, 7, 'Midterm Exam (out of 100)')
sheetn.write(0, 8, 'Final Exam (out of 100)')
sheetn.write(0, 9, 'Score')
sheetn.write(0, 10, 'Letter Grade')
for f in range(1, sheet.nrows):
    print('{}: score = {:.0f}, grade = {}'.format(name[f-1], agg[f-1], letter[f-1]))
    sheetn.write(f, 0, lname[f-1])
    sheetn.write(f, 1, fname[f-1])
    sheetn.write(f, 2, hw1[f-1])
    sheetn.write(f, 3, hw2[f-1])
    sheetn.write(f, 4, hw3[f-1])
    sheetn.write(f, 5, hw4[f-1])
    sheetn.write(f, 6, hw5[f-1])
    sheetn.write(f, 7, mid[f-1])
    sheetn.write(f, 8, fnl[f-1])
    sheetn.write(f, 9, agg[f-1])
    sheetn.write(f, 10, letter[f-1])
    
wbw.save(r"{}".format(loc2))


# In[ ]:





# In[ ]:




