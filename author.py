n = int(input())
a = list(set(map(int, input().strip().split())))[:n]
a.sort()
print(a[-2])
