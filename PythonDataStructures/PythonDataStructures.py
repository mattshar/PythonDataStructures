
# practicing some searching and sorting algorithms.

def bubbleSort(arr):
    flag = True  
    while flag:
        flag = False
        for x in range(1, len(arr)):
            if arr[x] < arr[x - 1]:
                flag = True      # flag is reset to True, allowing the loop to continue to run
                arr[x], arr[x-1] = arr[x-1], arr[x]
            


def binarySearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        midpoint = (left + right) // 2 
        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] < target:
            left = midpoint + 1     # only concerned with the right hand side
        else:
            right = midpoint - 1 # only concerned with the left hand side

    return -1 # target not found


def linearSearch(arr, target):
    for x in range(len(arr)):
        if arr[x] == target:
            return x
        
    return -1

