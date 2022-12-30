dict = {}
n = int(input())
for i in range(n):
    lines = str(input())
    if lines in dict:
        dict[lines] += 1
    else:
        dict[lines] = 1
res_1 = set(dict.keys())
print(len(res_1))
res_2 = [str(x) for x in dict.values()]
print(" ".join(res_2))