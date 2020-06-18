def bubbleSort(ar: [], n: int, debug=False):
    for i in range(n):
        for j in range(n - i - 1):
            if ar[j] > ar[j + 1]:
                ar[j], ar[j + 1] = ar[j + 1], ar[j]
        if debug:
            print("Pass No ", i + 1, ar)
    return ar


if __name__ == "__main__":
    ar = [10, 20, 30, 50, 40, 35, 23, 19, 9]
    print("before sorting in ASC ", ar)
    ar = bubbleSort(ar, len(ar), debug=True)
    print("after sorting in ASC ", ar)
