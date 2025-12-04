import timeit
import random


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

def generate_k_lists(sublists, el, max_value):
    lists = []
    for i in range(sublists):
        sublist = [random.randint(0, max_value) for _ in range(el)]
        sublist.sort()
        lists.append(sublist)
    return lists

def merge_k_lists(lists): 
    merged_list = lists[0] 
    for i in range(1, len(lists)): 
        merged_list = merge(merged_list, lists[i]) 
    return merged_list

def timing(lists):
    t_merge_k = timeit.timeit(lambda: merge_k_lists(lists[:]), number=1)
    print("***************************************")
    print(f"Merge k lists: {t_merge_k:.6f} секунд") 
    print("***************************************")

sublists = int(input("Введіть кількість підлистів: "))
el = int(input("Введіть кількість елементів у підлисті: "))
max_value = int(input("Введіть максмальне значення елемнта: "))

lists = generate_k_lists(sublists, el, max_value)

merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)

timing(lists)