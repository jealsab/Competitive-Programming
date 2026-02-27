n,k=map(int,input().split())
arr=list(map(int,input().split()))

arr.sort()

if k == 0:
    print(1 if arr[0] > 1 else -1)
elif k < n and arr[k] == arr[k-1]:
    print(-1)
else:
    print(arr[k-1])