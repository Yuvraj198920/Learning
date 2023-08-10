# start -> compare 1st value -> 

# 10 =  -> 5 -> 8 -> 9 -> 10
# 20 =  -> 10 -> 15 -> 17 -> 19 -> 20
# 40 =  -> 20 -> 30 -> 35 -> 37 -> 39 -> 40

steps = 0

def binary_search (arr, low, high, target):
    if (high >= low):
        global steps
        steps += 1
        mid  = calculate_mid(low, high)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, low, mid-1, target)
        else:
            return binary_search(arr, mid+1, high, target)
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