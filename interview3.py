# you can write to stdout for debugging purposes, e.g.
print("This is a debug message")
#(k) = arr[n-1] -> arr[k-1]
#arr2 
#loop through arr()i:
    # arr2[i+k % n] = arr[i]

#i+k % n
   #if i+k < n
        
    #else:
       #arr2[k+i-n] = arr[i]   c= 2; i = 2; c = 0   d=3; d=1 e=4; e=2  k

#temp = k-1
# i + k > n-1 
# arr[i] = arr[i+k]

# i+k 


def rotate(arr, k):
    n = len(arr)
    arr2 = [0] * n    #Space 0(n)
    for i in range(n):    #Time O(n)
        index = (i+k) % n
        arr2[index] = arr[i]
    return arr2

arr = ['a', 'b', 'c', 'd', 'e']
k = 3
print(rotate(arr, k))