arr = [3,1,9,5,6,7]

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
            
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

sort_arr= selection_sort(arr)
print(sort_arr)
