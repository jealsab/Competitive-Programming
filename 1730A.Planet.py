from collections import Counter
n=int(input())
for i in range(n):
    l,c=map(int,input().split())
    orbit=list(input().split())
    d=Counter(orbit)
    # print(d)
    min_cost=0
    for i in d:
        if d[i]< c:
            min_cost+=d[i]
        else:
            min_cost+=c
    print(min_cost)