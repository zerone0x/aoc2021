# depths = []
# with open('aoc1.txt', "r") as f:
#     for line in f:
#         line = line.strip()
#         line = int(line)
#         # print(line) 
#         depths.append(line)
#     print(depths)

#     count = 0
#     for i, num in enumerate(depths[:-1]):
#         if int(num) < int(depths[i + 1]):    # Compare previous with the current
#             count += 1

#     print(count)
# from itertools import pairwise

with open('aoc1.txt', "r") as f:
    depths = [int(x) for x in f]

    count = 0
    for i in range(3, len(depths)):
        left = depths[i - 3] + depths[i - 2] + depths[i - 1]
        right =  depths[i - 2] + depths[i - 1] + depths[i]
        if left < right:
            count += 1

    print(count)