def permutate(arr, start, stop):
  n = len(arr)
  
  if start == stop:    #when we reach the end
    print arr
    
  else:
    for i in range(start, stop+1):
      arr[start], arr[i] = arr[i], arr[start]
      permutate(arr, start+1, stop)
      arr[start], arr[i] = arr[i], arr[start]  #backtrack
      
arr = [1, 2, 3]
n = len(arr)
      
permutate(arr, 0, n-1)