# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    i = j = k = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] > arrB[j]:
            merged_arr[k] = arrB[j]
            j += 1
            
        else:
            merged_arr[k] = arrA[i]
            i += 1
        k += 1
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1 
        k += 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1






    # Your code here

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) == 0:
        return arr
    if len(arr) == 1:
        return arr
    if len(arr) > 1:
        middle = len(arr)//2 if len(arr) > 3 else 1

        left = arr[:middle] if len(arr) > 2 else [arr[0]]
        right = arr[middle:] if len(arr) > 2 else [arr[1]]

        if len(left) > 1:
            left = merge_sort(left)

        if len(right) > 1:

            right = merge_sort(right)

        arr = merge(left, right)

        return arr
    #Dive the arrays
    
        # recursively call merge_sort() on LHS
        # recursively call merge_sort() on RHS
        # merge sorted pieces
    # Your code here
print(merge_sort([10, 110, 5, 50, 1, 3, 2, 5, 10]))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
    # Your code here


#def merge_sort_in_place(arr, l, r):
    # Your code here
