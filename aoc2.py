import string
content = []
with open('aoc2.txt', "r") as f:
    # content = f.readlines()
    for line in f:
        line = line.strip()
        content.append(line)
    print(content)
horiz = 0
depth = 0
aim = 0
for cmd in content:
    num = int(cmd.strip(string.ascii_letters))
    if 'down' in cmd:
        aim += num
    elif 'up' in cmd:
        aim -= num
    elif 'forward' in cmd:
        horiz += num
        depth += (aim*num)
print({horiz*depth})