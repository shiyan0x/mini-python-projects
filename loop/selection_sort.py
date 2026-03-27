def selection_sort(arr):
  n = len(arr)
  for i in range(n-1):
    min_index = i
    for j in range(i+1,n):
      if arr[j]<arr[min_index]:
        min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

  return arr

arr = [65,34,32,67,23,2,35,11]
print("sorted array", selection_sort(arr))