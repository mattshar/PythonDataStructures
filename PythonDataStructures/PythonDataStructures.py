
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


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Splitting the list in half
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merging the sorted halves
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # Comparing elements from both lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

 
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Example
numbers = [8, 3, 5, 2, 7, 4]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)