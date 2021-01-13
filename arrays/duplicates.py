def duplicates(string):

    index = 0
    for i in range(0, len(string)):
        for j in range(0, i+1):
            if string[i] == string[j]:
                break
        
        if j == i:
            string[index] = string[i]
            index += 1

    return "".join(string[:index])


#print(duplicates(list('geeksforgeeks')))


def deleteArr(arr, num):
    n = len(arr)
    size = n
    for i in range(n):
        if arr[i] == num:
            #print(arr[i])
            for j in range(i, n-1):
                print(arr[j], arr[j+1])
                arr[j] = arr[j+1]
            size -= 1
    return arr[:size]


arr = [3, 5, 6, 7, 7, 8, 1, 3, 7]

print(deleteArr(arr, 7))