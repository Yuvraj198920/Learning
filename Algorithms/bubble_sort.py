def bubble_sort(ar):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):
            # swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 90, 22, 11, 12]
bubble_sort(arr)
print(f"Sorted array is: {arr}")

def find_highest(arr):
    n= len(arr)

    for i in range(n):
        highest = arr[i]
        for j in range(n-1):
            if highest < arr[j]:
                highest = arr[j]
    return highest

highest_number = find_highest(arr)
print(f"Highest number is: {highest_number}")