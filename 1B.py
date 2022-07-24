f = open('27b.txt')
n = int(f.readline())
a = [-1000000000] * 8
a[0] = 0
for i in range(n):
    x, y = map(int, f.readline().split())
    a_new = [-1000000000] * 8
    for j in range(8):
        jj = j + x
        a_new[jj % 8] = max(a[j] + x, a_new[jj % 8])
    for j in range(8):
        jj = j + y
        a_new[jj % 8] = max(a[j] + y, a_new[jj % 8])
    a = a_new[::]
print(a[3])

