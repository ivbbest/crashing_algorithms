def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [elem for elem in array[1:] if elem <= pivot]
        greatest = [elem for elem in array[1:] if elem > pivot]

        return quicksort(less) + [pivot] + quicksort(greatest)


print(quicksort([1, 2, 55, 3, 33, 4, 6, 7, 777, 8, 9, 77, 10, 11, 24]))
