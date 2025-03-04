def quickSort(arr):
  
  if len(arr)<=1:
    return arr
  
  mid = len(arr) // 2
  pivot = arr[mid]
  
  left = [x for x in arr if x < pivot]
  right = [x for x in arr if x> pivot]
  mid = [x for x in arr if x==pivot]
  
  return quickSort(left) + mid + quickSort(right)
  


if __name__ == "__main__":
  arr = [13,12,2,2,4,5,45,6,92,17]
  
  print(quickSort(arr))