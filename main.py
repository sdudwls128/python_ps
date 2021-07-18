d = [[]*10 for _ range(10)]
for i in range(10):
    d[i] = list(map(int, input().split()))

x = 1
y = 1

while 1:
    d[x][y] = 9
    if d[x][y+1] == 1:
        if d[x+1][y] == 1:
            break
        else:
            x += 1
        y += 1
    elif d[x][y+1] == 1:
        if d[x+1][y] == 0:
            x += 1
        elif d[x+1][y] == 1:
            break
    if d[x][y] == 2:
        d[x][y] = 9
        break
    if x==9 and y==9:
        d[x][y] = 9
        break