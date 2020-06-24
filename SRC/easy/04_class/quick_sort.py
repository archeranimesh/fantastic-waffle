# Quick Sort :  last element as pivot
def quick_sort_last_elem_pivot(arr, low, high):
    if low < high:
        print(low, high, arr)
        pivot_location = partitionC(arr, low, high)
        quick_sort_last_elem_pivot(arr, low, pivot_location - 1)
        quick_sort_last_elem_pivot(arr, pivot_location + 1, high)


def partitionA(arr, low, high):
    pivot = high
    leftwall = low
    print("\t", pivot, leftwall, arr[leftwall], arr)
    i = low + 1
    for i in range(low, high):
        if arr[i] < arr[pivot]:
            arr[i], arr[leftwall] = arr[leftwall], arr[i]
            leftwall = leftwall + 1
            # print("hello")
    arr[pivot], arr[leftwall] = arr[leftwall], arr[pivot]
    print("\t", pivot, leftwall, arr[leftwall], arr)
    return leftwall


def partitionB(arr, low, high):
    i = low
    p = high
    leftwall = low
    for i in range(low, high):
        if arr[i] < arr[p]:
            arr[i], arr[leftwall] = arr[leftwall], arr[i]
            leftwall += 1
    arr[p], arr[leftwall] = arr[leftwall], arr[p]
    return leftwall


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def partitionC(arr, left, right):
    pivot = left
    i = left
    j = right - 1
    while i < j:
        print(i, pivot)
        while arr[i] <= arr[pivot] and i < right:
            print(i)
            i += 1
        j -= 1
        print(j, pivot)
        while arr[j] > arr[pivot]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[pivot], arr[j] = arr[j], arr[pivot]
    return j


if __name__ == "__main__":
    arr = [10, 9, 1, 3, 4, 7, 2]
    print(arr)
    quick_sort_last_elem_pivot(arr, 0, len(arr) - 1)
    print(arr)
