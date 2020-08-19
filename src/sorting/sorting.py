# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Your code here

    while len(arrA) > 0 and len(arrB) > 0:  # if both arrays are > 0 basecase
        if arrA[0] < arrB[0]:  # if arrA is less than arrB index 0
            # append popped 0 index of array A to merged
            merged_arr.append(arrA.pop(0))
        else:
            # append popped 0 index of B array to merged
            merged_arr.append(arrB.pop(0))
    while len(arrA) > 0:
        # append popped 0 index of array A to merged
        merged_arr.append(arrB.pop(0))
    while len(arrB) > 0:
        # append popped 0 index of array B to merged
        merged_arr.append(arrB.pop(0))

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) > 1:  # if the length of the array is greater than 1
        mid = len(arr)//2  # split at the middle
        l = arr[:mid]  # the left half is everything from start to mid
        r = arr[mid:]  # the right half is everything from mid to end

        # return using helper fn merge with merge_sort l and merge_sort r as arrA and arrB replacements
        return merge(merge_sort(l), merge_sort(r))
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
