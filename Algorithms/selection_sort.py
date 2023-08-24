arr = [3,1,9,5,6,7]

def selection_sort(arr):
    for i in range(len(arr)):
        # hold the index of minimum element
        min_index = i
        for j in range(i+1, len(arr)):
            # check if element at min_index is greater than next element
            if arr[min_index] > arr[j]:
                min_index = j
        # swap the elememnts
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

sort_arr= selection_sort(arr)
print(sort_arr)
