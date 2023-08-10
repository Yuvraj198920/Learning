# start -> compare 1st value -> 

# 10 =  -> 5 -> 8 -> 9 -> 10
# 20 =  -> 10 -> 15 -> 17 -> 19 -> 20
# 40 =  -> 20 -> 30 -> 35 -> 37 -> 39 -> 40

steps = 0

def binary_search (arr, low, high, target):
    if (high >= low):
        global steps
        # to check how many recurrsion it took to find the target element
        steps += 1
        # Find mid
        mid  = calculate_mid(low, high)
        # if mid is the target element
        if arr[mid] == target:
            return mid
        # if the target elemet is lesser than mid then it is in the left portion of the array
        elif arr[mid] > target:
            return binary_search(arr, low, mid-1, target)
        # if the target elemet is greater than mid then it is in the right portion of the array
        else:
            return binary_search(arr, mid+1, high, target)
    # if target element not found 
    else:
        return -1
    
def calculate_mid(low, high):
    mid = low + (high - low)//2
    return mid
    
if __name__=='__main__':
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    search = binary_search(arr,0, len(arr)-1, 8)
    print(search)
    print(steps)