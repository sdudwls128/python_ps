d = [[0]*10 for _ in range(10)]
for i in range(10):
    d[i] = list(map(int, input().split()))
x = 1
y = 1
d[x][y] = 9

while x < 10 and y < 10:
    if d[x][y] == 2:
        d[x][y] = 9
        break
    if d[x][y+1] != 1:
        y += 1
    elif d[x+1][y] != 1:
        x += 1
    else:
        break
    d[x][y] = 9

for i in range(10):
    for j in range(10):
        print(d[i][j], end=' ')
    print()