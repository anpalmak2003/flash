f = open('27a.txt')
n = int(f.readline())
ans = 0
a = [int(f.readline()) for i in range(n)]
for start in range(n):
    for finish in range(start+1, n):
        s = 0
        for i in range(start,finish):
            if a[i]%8!=0:
                break
            s+=a[i]
        ans = max(s,ans)
print(ans)

