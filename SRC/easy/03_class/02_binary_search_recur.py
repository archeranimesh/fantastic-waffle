def binary_search_recur(ar, item, left, right, debug=False) -> int:
    if debug:
        print("left= ", left, " right= ", right)
    if left <= right:
        mid = (left + right) // 2
        if ar[mid] == item:
            return mid
        elif item > ar[mid]:
            return binary_search_recur(ar, item, mid + 1, right)
        else:
            return binary_search_recur(ar, item, left, mid - 1)


if __name__ == "__main__":
    primes = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
    ]
    number = 67
    left = 0
    right = len(primes)
    index = binary_search_recur(primes, number, left, right, debug=False)
    print(index)
