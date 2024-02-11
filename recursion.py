def get_arr_number(num: int):
    if num <= 1:
        return 0
    else:
        yield num
        yield get_arr_number(num - 1)


def fac(n):
    if n == 1:
        return 1
    return fac(n - 1) * n


# print(fac(5))

# arr = [print(g) for g in get_arr_number(10)]

# сумма элементов в списке
def sum_list(lst: list) -> int:
    return 0 if len(lst) == 0 else lst.pop() + sum_list(lst)


# print(sum_list([1,2,3,4,6,7, 8, 9, 10, 11]))

# подсчет количества в списке
def count_list(lst: list) -> int:
    return 0 if lst == [] else 1 + count_list(lst[1:])


print(count_list([1, 2, 3, 4, 6, 7, 8, 9, 10, 11]))


# найти наибольшее число в списке
def max_list(lst: list) -> int:
    if len(lst) == 1:
        return lst[0]
    else:
        max_list(lst[1:])
