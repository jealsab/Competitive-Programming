n, t = map(int, input().split())
a = list(map(int, input().split()))

l = 0
curr = 0
ans = 0

for r in range(n):
    curr += a[r]

    while curr > t:
        curr -= a[l]
        l += 1

    ans = max(ans, r - l + 1)

print(ans)