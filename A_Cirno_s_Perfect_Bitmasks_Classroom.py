test_case = int(input())
for i in range(test_case):
    n = int(input())
    if n == 1:
        print(3)
    else:   
        nearest_one_on=(n &(-1*n))
        if nearest_one_on&n > 0 and nearest_one_on^n >0:
            print(nearest_one_on) 
        else:
            if nearest_one_on%2 ==0:
                nearest_one_on+=1
            else:
                nearest_one_on-=1
            print(nearest_one_on)
