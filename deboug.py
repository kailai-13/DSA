def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    i=j=0
    re=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            re.append(left[i])
            i+=1
        else:
            re.append(right[j])
            j+=1

    re.extend(left[i:])
    re.extend(right[j:])

    return re

arr=[1,4,2,57,33]

print(merge_sort(arr))