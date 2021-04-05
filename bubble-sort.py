def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
  # for i in range(n-1):
    print('i is', i)
    for j in range(n-i-1):
    # for j in range(0, n-i-1):
      print('j is', j)
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j +1], arr[j]
    


nums = [5, 3, 8, 6]
bubble_sort(nums)
print(f"nums should be [3, 5, 6, 8] and is, in fact: {nums}")
