# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
        mid = start + (end - start)//2
        if len(arr) == 0:
            return -1
        elif arr[mid] == target:
                return mid
        elif arr[mid]>target:
            return binary_search(arr, target, start, mid-1)
        elif arr[mid]<target:
            return binary_search(arr, target, mid+1, end)
        else:
            return-1
# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
print(binary_search([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9], 1, -9, 9))
def agnostic_binary_search(arr, target):
    # Your code here
    pass
