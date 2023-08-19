"""Find the maximum product of two integers in an array where all elements are positive"""
# example :
# arr = [1, 7, 3, 4, 9, 5]
# max_product(arr) # Output: 63 (9*7)

def find_product(arr):
    first_large = 0
    second_large = 0
    for elem in arr:
        if elem > first_large:
            first_large = elem
    for elem_2 in arr:
        if elem_2 > second_large and elem_2 < first_large:
            second_large = elem_2
    return (first_large* second_large)
arr = [1, 7, 3, 4, 9, 5]
sum_of_large = find_product(arr)
print(sum_of_large)