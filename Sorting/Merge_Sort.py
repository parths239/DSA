# Implementation of MergeSort
def mergeSort(arr,start,end):
    if end<=start: # or e-s <= 0 
        return
        
    mid = (end+start) // 2
        
    mergeSort(arr,start,mid)
    mergeSort(arr,mid+1,end)
    merge(arr,start,mid,end)
    
def merge(arr,start,mid,end):
    left = arr[start:mid+1]
    right = arr[mid+1:end+1]
        
    i = 0
    j = 0
    k = start
        
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        
    while j < len(right): 
        arr[k] = right[j]
        j += 1
        k += 1    

def sort(arr):
    mergeSort(arr,0,len(arr)-1)
    return arr


##################

rollNumber = [12,52,22,1,5675,12,37,5]
print(sort(rollNumber))