from typing import List

a = [10, 20, 33, 44, 52]

sum = 0
for i in range(len(a)):
    sum += a[i]

print(sum)

# in operator implementation.
def is_present(a: List[int], item: int) -> bool:
    """
    in operator implementation
    """
    for i in range(len(a)):
        if a[i] == item:
            return True
    return False


print(is_present(a, 10))
a.sort()
print(a)
