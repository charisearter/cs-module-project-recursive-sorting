# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) > 1:  # if the length of the array is greater than 1
        mid = len(arr)/2  # split at the middle
        lefthalf = arr[:mid]  # the left half is everything from start to mid
        righthalf = arr[mid:]  # the right half is everything from mid to end

        merge_sort(lefthalf)  # keep going until it is 1 -> recursive call
        merge_sort(righthalf)  # keep going until it is 1
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    pass
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
