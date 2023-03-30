size_nums1, size_nums2= list(map(int,input().split()))
nums1 = list(map(int,input().split()))
nums2=list(map(int,input().split()))
res = []
i = 0
j = 0
while i < size_nums1 and j < size_nums2:
    if nums1[i] < nums2[j]:
        res.append(nums1[i])
        i+=1    
    else:
        res.append(nums2[j])
        j+=1
        
while i < size_nums1:
    res.append(nums1[i])
    i += 1
while j < size_nums2:
    res.append(nums2[j])
    j += 1
 
print(*res)
