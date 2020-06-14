


def binary_search(sorted_list, number, debug=False):
    min = 0
    max = len(sorted_list) - 1
    result = -1
    while max > min:
        mid = (min + max) // 2
        if debug:
            print(min, max, mid, sorted_list[min], sorted_list[max], sorted_list[mid])
        if sorted_list[mid] == number:
            result = mid
        if sorted_list[mid] < number:
            min = mid + 1
        else:
            max = mid - 1 
    return result

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
    number = 68

    index = binary_search(primes, number)
    print(index, primes[index])
