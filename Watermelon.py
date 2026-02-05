weight=int(input())
def two_parts(w):
    if weight%2==0 and weight!=2:
        return "YES"
    return "NO"
print(two_parts(weight))