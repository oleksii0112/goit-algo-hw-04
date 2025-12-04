import random
import timeit


def generate_array(max_quantity, max_value):
    arr = []

    for n in range(max_quantity):
        arr.append(random.randint(0, max_value))
    return arr

def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):

    if len(arr) <= 1:
        return arr 
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    return merged

def timing_compare(arr):

    print(f"Розмір масиву: {len(arr)}")

    t_insertion = timeit.timeit(lambda: insertion_sort(arr[:]), number=1)
    print(f"Insertion sort: {t_insertion:.6f} секунд")
     
    t_merge = timeit.timeit(lambda: merge_sort(arr[:]), number=1)
    print(f"Merge sort: {t_merge:.6f} секунд")

    t_timsort = timeit.timeit(lambda: sorted(arr[:]), number=1)
    print(f"Timsort (built-in sorted): {t_timsort:.6f} секунд")

if __name__ == "__main__":
    max_quantity = int(input("Введіть розмір масиву: "))
    max_value = int(input("Введіть максимальне значення числа: "))
    test_array = generate_array(max_quantity, max_value)
    timing_compare(test_array)