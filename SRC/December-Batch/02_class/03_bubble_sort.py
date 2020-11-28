from typing import List

a = [10, 20, 54, 44, 52]


def bubble_sort(a: List[int]):
    """
    docstring
    """
    # Outer loop
    for i in range(len(a)):
        # inner loop, carefull
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


# Oprimized version
def bubble_sort_2(a: List[int]):
    """
    docstring
    """
    # Outer loop
    for i in range(len(a)):
        # inner loop, carefull
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


bubble_sort_2(a)
print(a)
