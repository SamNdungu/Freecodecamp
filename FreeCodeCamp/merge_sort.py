# Sorting algorithm uses divide_and_conquer principle to sort collections of data. i.e it divides a collection into smaller sub-parts and 'conquers' the sub-parts by sorting them independently, then merges the sorted sub-parts.

def merge_sort(array):
    if len(array) <= 1:
        return
    
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


if __name__ == '__main__':
    numbers = [17, 5, 29, 12, 8, 24, 3, 21, 14, 27, 19, 6, 23, 11, 9, 16, 28, 7, 26, 2, 20, 15, 30, 22, 10, 25, 1, 18, 4, 13]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
    print('Sorted array: ' + str(numbers))
