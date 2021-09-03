n = int(input())
a = list(map(int, input().strip().split()))[:n]
mx = max(a)
ans = -101
for x in a:
    if x > ans and x != mx:
        ans = x

print(ans)
