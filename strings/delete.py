'''
Question 1: Implement a simple autocorrect
Clarifying questions -> 
1. Efficiency is to how many chars? -> Assumption system is correct to only one char
2. Is it online/ offline
    For online -> it would need to be first so we might need to implement 
    a cache of recently used words
3. Is it case sensitive?
4. Alphabets? numbers? symbols? allowed
'''

from collections import OrderedDict                     #To maintain the order of our dict
wordStore = ['term', 'terms', 'terminal']             #
alphabets = 'abcdefghijklmnopqrstuvwxyz'

#Function to check if our number exists in the word store
def inWordStore(wordstore, word):
    if word in wordstore:
        return True
    else:
        return False

'''
Simple insert function -> 
Append each char of the alphabet to all the positions of the characters in the word
Use string concatenation
'''
def simpleInsert(word):
    for i in range(len(word) + 1):
        for char in alphabets:
            newword = word[:i] + char + word[i:]
            if inWordStore(wordStore, newword):
                print(newword)
                return newword
    print('No word has a 1 character simple insert in the word store')


'''
Simple delete function -> 
At each position of the characters in the word, delete the char and concatenate the 
start and ends
'''
def simpleDelete(word):
    for i in range(len(word)):
        newword = word[:i] + word[(i+1):]
        if inWordStore(wordStore, newword):
            print(newword)
            return newword
    print('No word has a 1 character simple delete in the word store')

'''
Simple replace function -> S
At each position of the word, replace the existing char with a char of the alphabet
'''
def simpleReplace(word):
    for i in range(len(word)):
        for char in alphabets:
            if word[i] != char:
                newword = word[:i] + char + word[i+1:]
                if inWordStore(wordStore, newword):
                    print (newword)
                    return newword
    print('No word has a 1 character simple replace in the word store')


simpleReplace('tern')
simpleInsert('timo')
simpleDelete('terma')

def delete(word, c):
    for i in range(len(word)):
        if ( word[i] == c ):
            pos = i
            print (pos)

    return word[:pos] + word[(pos+1):]

#print(delete('termes', 'e'))

'''
Create a dict to store the nums in the array and their frequency
Create a new arr to store the unique nums
Loop through the dict and for any value that is more than 1, 
we know that it contains duplicates
'''

def deleteDuplicates(arr):
    myDict = OrderedDict()   #use an ordered dict to preserve order
    newarr = list()
    
    i = 0
    for a in arr:                    # O(n)
        if a not in myDict:
            myDict[a] = 1
        else:
            myDict[a] += 1

        print(myDict)
    
    for key in myDict:               #O(m)
        if myDict[key] == 1:
            newarr.append(key)
            i += 1
    return newarr


'''
We cannot change the array in place because it will affect subsequent duplicates
Time complexity is O(n^2) and there is extra space(m) for the new array

'''
def findUnique(arr):
    newarr = []
    firstUnique = -1
    for i in range(len(arr)):
        flag = True
        for j in range(len(arr)):    #O(n)
            if arr[i] == arr[j] and i != j:   #O(n)
                flag = False
        if flag == True:
            newarr.append(arr[i])
            firstUnique = arr[i]
            #break

    return newarr

print(findUnique([3, 5, 6, 7, 7, 8, 1, 3]))

#print(deleteDuplicates([3, 5, 6, 7, 7, 8, 1, 3]))
