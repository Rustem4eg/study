def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for t in range(0, n-i-1):
            if arr[t] > arr[t+1]:
                arr[t], arr[t+1] = arr[t+1], arr[t]

my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Отсортированный список:", my_list)