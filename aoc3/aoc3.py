import numpy
content = []
with open('aoc3.txt', "r") as f:
    # content = f.readlines()
    for line in f:
        line = line.strip()
        content.append(line)
    # print(content)
one = [[0 for i in range(2)] for j in range(12)]
print(one)
# two = numpy.zeros((12, 1))
two = [0 for j in range(12)]
print(two)
for cmd in content:
    print('cmd',cmd)
    print('first',cmd[0])
    if cmd[0] == '0':
        one[0][0] +=1
    else:
        one[0][1] +=1
    if cmd[1] == '0':
        one[1][0] +=1
    else:
        one[1][1] +=1
    if cmd[2] == '0':
        one[2][0] +=1
    else:    
        one[2][1] +=1           
    if cmd[3] == '0':
        one[3][0] +=1           
    else:    
        one[3][1] +=1
    if cmd[4] == '0':
        one[4][0] +=1   
    else:   
        one[4][1] +=1
    if cmd[5] == '0':
        one[5][0] +=1
    else:
        one[5][1] +=1
    if cmd[6] == '0':
        one[6][0] +=1
    else:   
        one[6][1] +=1
    if cmd[7] == '0':
        one[7][0] +=1
    else:
        one[7][1] +=1
    if cmd[8] == '0':
        one[8][0] +=1
    else:   
        one[8][1] +=1
    if cmd[9] == '0':
        one[9][0] +=1
    else:
        one[9][1] +=1
    if cmd[10] == '0':
        one[10][0] +=1
    else:
        one[10][1] +=1
    if cmd[11] == '0':
        one[11][0] +=1
    else:
        one[11][1] +=1

if one[0][0] > one[0][1]:
    two[0]=0
else:
    two[0]=1
if one[1][0] > one[1][1]:
    two[1]=0    
else:
    two[1]=1
if one[2][0] > one[2][1]:
    two[2]=0
else:
    two[2]=1
if one[3][0] > one[3][1]:
    two[3]=0
else:
    two[3]=1
if one[4][0] > one[4][1]:
    two[4]=0
else:
    two[4]=1
if one[5][0] > one[5][1]:
    two[5]=0
else:
    two[5]=1
if one[6][0] > one[6][1]:
    two[6]=0
else:
    two[6]=1
if one[7][0] > one[7][1]:
    two[7]=0
else:
    two[7]=1
if one[8][0] > one[8][1]:
    two[8]=0
else:
    two[8]=1
if one[9][0] > one[9][1]:
    two[9]=0
else:
    two[9]=1
if one[10][0] > one[10][1]:
    two[10]=0
else:
    two[10]=1
if one[11][0] > one[11][1]:
    two[11]=0
else:
    two[11]=1
# print(two[0],two[1],two[2],two[3],two[4],two[5],two[6],two[7],two[8],two[9],two[10],two[11])
