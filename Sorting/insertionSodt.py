def insertionSort(arr):
  
  for i in range(1,len(arr)):
    
    j = i-1
    while j>=0 and arr[j+1]<arr[j]:
      temp = arr[j]
      arr[j] = arr[j+1]
      arr[j+1] = temp
      j-=1
  
  return arr


if __name__ == "__main__":
  arr = [13,12,2,4,5,45,6,92,17]
  
  print(insertionSort(arr))