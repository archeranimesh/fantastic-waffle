# Quick Sort :  last element as pivot
def quick_sort_last_elem_pivot(arr, low, high):
    if low < high:
        print(low, high)
        pivot_location = partitionA(arr, low, high)
        quick_sort_last_elem_pivot(arr, low, pivot_location - 1)
        quick_sort_last_elem_pivot(arr, pivot_location + 1, high)


def partitionA(arr, low, high):
    pivot = arr[low]
    leftwall = low + 1
    for i in range(low, high):
        if arr[i] < pivot:
            leftwall = leftwall + 1
            arr[i], arr[leftwall] = arr[leftwall], arr[i]
    arr[low], arr[leftwall] = arr[leftwall], arr[low]
    return leftwall - 1


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    arr = [10, 9, 1, 3, 4, 7, 2]
    print(arr)
    quick_sort_last_elem_pivot(arr, 0, len(arr) - 1)
    print(arr)
