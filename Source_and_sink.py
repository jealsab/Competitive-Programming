from collections import defaultdict
n = int(input())
src_graph = defaultdict(list)
dest_graph=defaultdict(list)
src=[]  
dest=set() 
for i in range(n):
    dest.add(i+1)
        
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        src_graph[i].append(row[j])
    if 0 in src_graph[i] and len(set(src_graph[i]))==1:
        src.append(i+1)
    for x in range(len(row)):
        if row[x]==0:
            pass
        else:
            if x+1 in dest:
                dest.remove(x+1)
final_dest= [len(dest)]
final_dest.extend(dest)               
src_res=[len(src)]
src_res.extend(src)
print(*final_dest)  
print(*src_res)

