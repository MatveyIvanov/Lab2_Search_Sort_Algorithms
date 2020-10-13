import time, random, copy

from Lab2_Sort_Search_Algorithms import insertion_sort, quick_sort


def get_time_insertion_sort(arr):
    start_time = time.time() * 1000
    insertion_sort(arr)
    return time.time() * 1000 - start_time # In milliseconds

def get_time_quick_sort(arr):
    start_time = time.time() * 1000
    quick_sort(arr, 0, len(arr) - 1)
    return time.time() * 1000 - start_time # In milliseconds


with open('time_tests.txt', 'w') as f:
    f.write('Insertion sort(size = 10) | Quick sort(size = 10)\n')
    insertion_sort_total_time = 0
    quick_sort_total_time = 0
    for _ in range(10):
        lst1 = [random.randint(1, 10000) for i in range(10)]
        lst2 = copy.deepcopy(lst1)
        insertion_sort_time = get_time_insertion_sort(lst1)
        quick_sort_time = get_time_quick_sort(lst2)
        insertion_sort_total_time += insertion_sort_time
        quick_sort_total_time += quick_sort_time
        f.write(str(insertion_sort_time) + ' | ')
        f.write(str(quick_sort_time) + '\n')
    f.write('Mean time of insertion sort: ' + str(insertion_sort_total_time / 10))
    f.write(' Mean time of quick sort: ' + str(quick_sort_total_time / 10))

    f.write('\n\n')
    f.write('Insertion sort(size = 100) | Quick sort(size = 100)\n')
    insertion_sort_total_time = 0
    quick_sort_total_time = 0
    for _ in range(10):
        lst1 = [random.randint(1, 10000) for i in range(100)]
        lst2 = copy.deepcopy(lst1)
        insertion_sort_time = get_time_insertion_sort(lst1)
        quick_sort_time = get_time_quick_sort(lst2)
        insertion_sort_total_time += insertion_sort_time
        quick_sort_total_time += quick_sort_time
        f.write(str(insertion_sort_time) + ' | ')
        f.write(str(quick_sort_time) + '\n')
    f.write('Mean time of insertion sort: ' + str(insertion_sort_total_time / 10))
    f.write(' Mean time of quick sort: ' + str(quick_sort_total_time / 10))

    f.write('\n\n')
    f.write('Insertion sort(size = 1000) | Quick sort(size = 1000)\n')
    insertion_sort_total_time = 0
    quick_sort_total_time = 0
    for _ in range(10):
        lst1 = [random.randint(1, 10000) for i in range(1000)]
        lst2 = copy.deepcopy(lst1)
        insertion_sort_time = get_time_insertion_sort(lst1)
        quick_sort_time = get_time_quick_sort(lst2)
        insertion_sort_total_time += insertion_sort_time
        quick_sort_total_time += quick_sort_time
        f.write(str(insertion_sort_time) + ' | ')
        f.write(str(quick_sort_time) + '\n')
    f.write('Mean time of insertion sort: ' + str(insertion_sort_total_time / 10))
    f.write(' Mean time of quick sort: ' + str(quick_sort_total_time / 10))

    f.write('\n\n')
    f.write('Insertion sort(size = 10000) | Quick sort(size = 10000)\n')
    insertion_sort_total_time = 0
    quick_sort_total_time = 0
    for _ in range(10):
        lst1 = [random.randint(1, 10000) for i in range(10000)]
        lst2 = copy.deepcopy(lst1)
        insertion_sort_time = get_time_insertion_sort(lst1)
        quick_sort_time = get_time_quick_sort(lst2)
        insertion_sort_total_time += insertion_sort_time
        quick_sort_total_time += quick_sort_time
        f.write(str(insertion_sort_time) + ' | ')
        f.write(str(quick_sort_time) + '\n')
    f.write('Mean time of insertion sort: ' + str(insertion_sort_total_time / 10))
    f.write(' Mean time of quick sort: ' + str(quick_sort_total_time / 10))

    f.write('\n\n')
    f.write('Insertion sort(size = 100000) | Quick sort(size = 100000)\n')
    insertion_sort_total_time = 0
    quick_sort_total_time = 0
    for _ in range(10):
        lst1 = [random.randint(1, 10000) for i in range(100000)]
        lst2 = copy.deepcopy(lst1)
        insertion_sort_time = get_time_insertion_sort(lst1)
        quick_sort_time = get_time_quick_sort(lst2)
        insertion_sort_total_time += insertion_sort_time
        quick_sort_total_time += quick_sort_time
        f.write(str(insertion_sort_time) + ' | ')
        f.write(str(quick_sort_time) + '\n')
    f.write('Mean time of insertion sort: ' + str(insertion_sort_total_time / 10))
    f.write(' Mean time of quick sort: ' + str(quick_sort_total_time / 10))
