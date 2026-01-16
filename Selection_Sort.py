def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
 
array = [50, 112, 321, 32, 4, 0]
print("Trước khi sắp xếp:", array)
sorted_array = selection_sort(array)
print("Sau khi sắp xếp:", sorted_array)