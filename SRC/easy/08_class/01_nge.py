# Next Greater Element
# https://www.geeksforgeeks.org/next-greater-element/


def getNextGreaterEle(arr):
    return_arr = []
    for i in range(len(arr)):
        next = -1
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                next = arr[j]
                break
        return_arr.append(next)
    return return_arr


if __name__ == "__main__":
    arr = [11, 13, 21, 3]
    print(getNextGreaterEle(arr))
