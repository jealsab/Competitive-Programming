
n,m = map(int, input().split())
 
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
i = 0
j = 0
res = []
 
while i < n and j < m:
    if arr1[i] < arr2[j]:
        i += 1
    else:
        res.append(i)    
        j += 1
while len(res) < m:
    res.append(i)
print(*res)