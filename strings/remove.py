def remove(string, remove):
    newString = ''
    for i in range(len(string)):
        for j in range(len(remove)):
            if string[i] == remove[j]:
                break

            newString += string[i]

    return newString


string = 'Battle of the Vowels: Hawaii vs. Grozny'
removeStr = 'aeiou'
print(remove(string, removeStr))
