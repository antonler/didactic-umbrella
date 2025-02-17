import random
import time
import matplotlib.pyplot as plt

# Генерация случайного массива
def generate_array(size, min_val=0, max_val=1000):
    return [random.randint(min_val, max_val) for _ in range(size)]

# 1. Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 2. Сортировка слиянием
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 3. Пузырьковая сортировка
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# 4. Сортировка выбором
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Линейный поиск
def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

# Бинарный поиск (работает только на отсортированном массиве)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Функции работы с массивами
def find_max(arr):
    return max(arr)

def find_min(arr):
    return min(arr)

def calculate_average(arr):
    return sum(arr) / len(arr)

# Измерение времени выполнения
def measure_time(func, arr, *args):
    start = time.time()
    result = func(arr, *args) if args else func(arr)
    return result, time.time() - start

# Визуализация массива
def plot_array(arr, title="Array Visualization"):
    plt.figure(figsize=(10, 5))
    plt.bar(range(len(arr)), arr, color='blue')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title(title)
    plt.show()

# Главная функция
def main():
    size = 50  # Размер массива
    max_value = 100
    array = generate_array(size, 0, max_value)

    print(f"Original Array: {array}\n")

    # Операции с массивом
    print(f"Max Value: {find_max(array)}")
    print(f"Min Value: {find_min(array)}")
    print(f"Average Value: {calculate_average(array):.2f}\n")

    # Сортировка и измерение времени
    times = {}
    sorted_list, times["Quick Sort"] = measure_time(quick_sort, array)
    _, times["Merge Sort"] = measure_time(merge_sort, array)
    _, times["Bubble Sort"] = measure_time(bubble_sort, array.copy())
    _, times["Selection Sort"] = measure_time(selection_sort, array.copy())

    for name, t in times.items():
        print(f"{name}: {t:.6f} sec")

    # Поиск элемента
    target = random.choice(sorted_list)
    lin_index, lin_time = measure_time(linear_search, sorted_list, target)
    bin_index, bin_time = measure_time(binary_search, sorted_list, target)

    print(f"Linear Search Time: {lin_time:.6f} sec, Found at index: {lin_index}")
    print(f"Binary Search Time: {bin_time:.6f} sec, Found at index: {bin_index}")

    # Визуализация массива
    plot_array(array, "Original Array")
    plot_array(sorted_list, "Sorted Array")

if __name__ == "__main__":
    main()