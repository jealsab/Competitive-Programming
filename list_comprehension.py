if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    res=[]
    for i in range (x+1):
        t =0
        for j in range(y+1):
            for k in range(z+1):
                t = i+j+k
                if t != n :
                    res.append([i,j,k])
    print(res)
              