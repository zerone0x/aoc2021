import numpy
content = []
with open('aoc3.txt', "r") as f:
    # content = f.readlines()
    for line in f:
        line = line.strip()
        content.append(line)
    # print(content)
one = [[0 for i in range(2)] for j in range(12)]
# two = numpy.zeros((12, 1))
two = [0 for j in range(12)]
for cmd in content:
    if cmd[0] == '0':
        one[0][0] +=1
    else:
        one[0][1] +=1
    

if one[0][0] > one[0][1]:
    two[0]=0
else:
    two[0]=1
ans = []
ans_0 = []
if(two[0] == 0):
    for cmd in content:
        if cmd[0] == '1':
            ans.append(cmd)
        # else:
        #     ans_0.append(cmd)
else:
    for cmd in content:
        if cmd[0] == '0':
            ans.append(cmd)
        # else:
        #     ans_0.append(cmd)
# print(ans)
# -------
for cmd in ans:
    if cmd[1] == '0':
        one[1][0] +=1
    else:
        one[1][1] +=1
# print(one[1][0], one[1][1])
if one[1][0] > one[1][1]:
    two[1]=0    
else:
    two[1]=1
print(two[1])
ans1 = []
if(two[1] == 0):
    for cmd in ans:
        if cmd[1] == '1':
            ans1.append(cmd)
else:
    for cmd in ans:
        if cmd[1] == '0':
            ans1.append(cmd)
# print(ans1)
# -------
for cmd in ans1:
    if cmd[2] == '0':
        one[2][0] +=1
    else:
        one[2][1] +=1

if one[2][0] > one[2][1]:
    two[2]=0
else:
    two[2]=1
ans2 = []

if(two[2] == 0):
    for cmd in ans1:
        if cmd[2] == '1':
            ans2.append(cmd)
else:
    for cmd in ans1:
        if cmd[2] == '0':
            ans2.append(cmd)
# print(ans2)

# -----------------
for cmd in ans2:
    if cmd[3] == '0':
        one[3][0] +=1
    else:
        one[3][1] +=1

if one[3][0] > one[3][1]:
    two[3]=0
else:
    two[3]=1
ans3 = []
# print(one[3][0], one[3][1])
if(two[3] == 0):
    for cmd in ans2:
        if cmd[3] == '1':
            ans3.append(cmd)
else:
    for cmd in ans2:
        if cmd[3] == '0':
            ans3.append(cmd)
# print(ans3)
# -----------------
for cmd in ans3:
    if cmd[4] == '0':
        one[4][0] +=1
    else:
        one[4][1] +=1

if one[4][0] > one[4][1]:
    two[4]=0
else:
    two[4]=1
ans4 = []
print(one[4][0], one[4][1])
if(two[4] == 0):
    for cmd in ans3:
        if cmd[4] == '1':
            ans4.append(cmd)
else:
    for cmd in ans3:
        if cmd[4] == '0':
            ans4.append(cmd)
# print(ans4)
# -----------------
for cmd in ans4:
    if cmd[5] == '0':
        one[5][0] +=1
    else:
        one[5][1] +=1

if one[5][0] > one[5][1]:
    two[5]=0
else:
    two[5]=1
ans5 = []
print(one[5][0], one[5][1])
if(two[5] == 0):
    for cmd in ans4:
        if cmd[5] == '1':
            ans5.append(cmd)
else:
    for cmd in ans4:
        if cmd[5] == '0':
            ans5.append(cmd)
# print(ans5)
# -----------------
for cmd in ans5:
    if cmd[6] == '0':
        one[6][0] +=1
    else:
        one[6][1] +=1

if one[6][0] > one[6][1]:
    two[6]=0
else:
    two[6]=1
ans6 = []
print(one[6][0], one[6][1])
if(two[6] == 0):
    for cmd in ans5:
        if cmd[6] == '1':
            ans6.append(cmd)
else:
    for cmd in ans5:
        if cmd[6] == '0':
            ans6.append(cmd)
# print(ans6)
# -----------------
for cmd in ans6:
    if cmd[7] == '0':
        one[7][0] +=1
    else:
        one[7][1] +=1

if one[7][0] > one[7][1]:
    two[7]=0
else:
    two[7]=1
ans7 = []
print(one[7][0], one[7][1])
if(two[7] == 0):
    for cmd in ans6:
        if cmd[7] == '1':
            ans7.append(cmd)
else:
    for cmd in ans6:
        if cmd[7] == '0':
            ans7.append(cmd)
print(ans7)
# -----------------
for cmd in ans7:
    if cmd[8] == '0':
        one[8][0] +=1
    else:
        one[8][1] +=1

if one[8][0] > one[8][1]:
    two[8]=0
else:
    two[8]=1
ans8 = []
print(one[8][0], one[8][1])
if(two[8] == 0):
    for cmd in ans7:
        if cmd[8] == '1':
            ans8.append(cmd)
else:
    for cmd in ans7:
        if cmd[8] == '0':
            ans8.append(cmd)
print(ans8)
# -----------------
for cmd in ans8:
    if cmd[9] == '0':
        one[9][0] +=1
    else:
        one[9][1] +=1

if one[9][0] > one[9][1]:
    two[9]=0
else:
    two[9]=1
ans9 = []
print(one[9][0], one[9][1])
if(two[9] == 0):
    for cmd in ans8:
        if cmd[9] == '1':
            ans9.append(cmd)
else:
    for cmd in ans8:
        if cmd[9] == '0':
            ans9.append(cmd)
print(ans9)
# -----------------
for cmd in ans9:
    if cmd[10] == '0':
        one[10][0] +=1
    else:
        one[10][1] +=1

if one[10][0] > one[10][1]:
    two[10]=0
else:
    two[10]=1
ans10 = []
print(one[10][0], one[10][1])
if(two[10] == 0):
    for cmd in ans9:
        if cmd[10] == '1':
            ans10.append(cmd)
else:
    for cmd in ans9:
        if cmd[10] == '0':
            ans10.append(cmd)
print(ans10)
# -------#
for cmd in ans10:
    if cmd[11] == '0':
        one[11][0] +=1
    else:
        one[11][1] +=1

if one[11][0] > one[11][1]:
    two[11]=0
else:
    two[11]=1
ans11 = []
print(one[11][0], one[11][1])
if(two[11] == 0):
    for cmd in ans10:
        if cmd[11] == '1':
            ans11.append(cmd)
else:
    for cmd in ans10:
        if cmd[11] == '0':
            ans11.append(cmd)
print(ans11)