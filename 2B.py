f = open('27B.txt')
n = int(f.readline())
ans = 0
cur_s = 0
for i in range(n):
    x = int(f.readline())
    if x%8 == 0:
        cur_s += x
    else:
        cur_s = 0
    ans = max(cur_s,ans)
print(ans)

