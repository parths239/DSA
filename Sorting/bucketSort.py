
def bucketSort(arr):
  
  bucket = [0,0,0]
  
  for element in arr:
    bucket[element] += 1
  
  # bucket = [2,2,3]
  # arr =[0,2,2,1,0,1,2]
  
  counter = 0
  for i in range(len(bucket)):
    for j in range(bucket[i]):
      arr[counter] = i
      counter += 1
    
  return arr



if __name__ == "__main__":
  arr = [0,2,2,1,0,1,2]
  
  print(bucketSort(arr))