arr = [3,1,9,5,6,7]

for i, elem in enumerate(arr):
    
    for j, elem2 in enumerate(arr[i+1:]):
        temp1=elem
        temp2=elem2
        if temp1>temp2:
            arr[i] = temp2
            arr[i+1] = temp1
            temp1=temp2


print(arr)