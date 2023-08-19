def partition(arr, low, high):
    i = (low-1)  # index of smaller element
    pivot = arr[high]
    for j in range(low, high):
        # if current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # increment the index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)
        # Seperately sort element before partition and after partition
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

sort_array = [64, 34, 25, 90, 22, 11, 12]
n = len(sort_array)
quick_sort(sort_array, 0, n-1)

print(f"Sorted array is: {sort_array}")