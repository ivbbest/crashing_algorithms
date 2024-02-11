# бинарный поиск циклом
def binary_search_classic(array: list, search_elem: int) -> int | None:
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = array[mid]
        if search_elem == guess:
            return mid
        elif search_elem > guess:
            low = mid + 1
        else:
            high = mid - 1

    return None


# print(binary_search_classic([1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 24, 33, 55, 77, 777], 23))

# бинарный поиск рекурсией
def binary_search_recursive(array: list, search_elem: int) -> int | None:
    # if len(array) < 2:
    #     return 0 if search_elem == array[0] else None
    # else:
    low = 0
    high = len(array) - 1
    mid = int((low + high) / 2)
    breakpoint()
    if search_elem == array[mid]:
        return mid
    elif search_elem > array[mid]:
        return binary_search_recursive(array[mid + 1:], search_elem)

    return binary_search_recursive(array[:mid], search_elem)


# бинарные поиск через стандартную библиотеку
import bisect


def binary_search_bisect(arr, x):
    i = bisect.bisect_left(arr, x)
    breakpoint()
    if i != len(arr) and arr[i] == x:
        return i
    else:
        return -1


print(binary_search_recursive([1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 24, 33, 55, 77, 777], 24))
