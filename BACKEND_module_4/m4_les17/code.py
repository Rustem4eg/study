def insertion_sort(arr):
    for i in range(1, len(arr)):
        cur_item = arr[i]

        k = i - 1
        while k >=0 and arr[k] > cur_item:
            arr[k+1] = arr[k]
            k -= 1

        arr[k+1] = cur_item


# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_list)
print("Отсортированный список:", my_list)