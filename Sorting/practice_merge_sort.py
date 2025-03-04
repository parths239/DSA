def sort(array):
  
  merge_sort(array,0,len(array))
  return array

def merge_sort(array, start, end):
  if end<=start:
    return
  
  mid = (start+end) // 2
  
  merge_sort(array,start,mid)
  merge_sort(array,mid+1,end)
  merge(array,start,mid,end)
  
def merge(array, start, mid, end):
  
  left = array[start:mid+1]
  right = array[mid+1:end+1]
  
  i = 0
  j = 0
  k = start
  
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      array[k] = left[i]
      i+=1
      k+=1
    else:
      array[k] = right[j]
      j+=1
      k+=1
  
  while i < len(left):
    array[k] = left[i]
    i+=1
    k+=1
    
  while j < len(right):
    array[k] = right[j]
    j+=1
    k+=1

if __name__ == "__main__":
  arr = [13,12,2,4,5,45,6,92,17]
  
  print(sort(arr))