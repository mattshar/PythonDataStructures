
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


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = [4, 10, 3, 5, 1]
heap_sort(arr)
print("Sorted array:", arr)