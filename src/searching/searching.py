# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    while start < end:
        middle = (start + end)//2  # // so it will be int not float
        if target == middle:  # if target is middle
            return middle  # return the middle
        elif target < arr[middle]:  # if target is less than middle
            # end = arr[:middle-1]  # remove right side of middle
            return binary_search(arr, target, start, (middle - 1))
        elif target > arr[middle]:  # if target is greater than array
            # start = arr[middle+1:]  # remove the left side of middle
            return binary_search(arr, target, (middle + 1), end)
    return -1  # return this if not found


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
