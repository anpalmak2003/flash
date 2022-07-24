f = open('27a.txt')
n = int(f.readline())
ans = 0
mask = []
a = [map(int, f.readline().split()) for i in range(n)]
for i in range(2 ** n):
    t = i
    mask_i = []
    for j in range(n):
        mask_i.append(t % 2)
        t //= 2
    mask.append(mask_i)
for m in mask:
    s = 0
    j = 0
    for i in m:
        s += a[j][i]
        j += 1
    if s % 8 == 3:
        ans = max(ans, s)
print(ans)
