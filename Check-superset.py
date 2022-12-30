# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(map(int, input().split()))
n = int(input())
superset = 1
for i in range(n):
    sets = set(map(int, input().split()))
    if len(a) > len(sets):
        for num in sets:
            if num not in a:
                superset = 0
                break
    else:
        superset = 0
        break
                
if superset == 1:
    print(True)
else:
    print(False)