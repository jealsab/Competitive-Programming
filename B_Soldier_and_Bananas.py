k,n,w =map(int, input().split())
total=0
v = 1
for i in range (1,w+1):
    v = k*i
   
    total+=v
    
if total-n>0:
    print(total-n)
else:
    print("0")