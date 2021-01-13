def alphaCount(inputStr):
    count = 0
    alpha = ''

    for i in range(0, len(inputStr)):
        if inputStr[i].isdigit():
            count = int(str(count) + str(inputStr[i]) )
            #print(count)
        elif inputStr[i].isalpha():
            alpha = inputStr[i]
            #print( alpha * int(count))
            count = ''
            alpha = ''

        else:
            return

def alphaCount2(inputStr):
    count = 0
    alpha = ''

    for i in range(1, len(inputStr)+1):
        if inputStr[i].isalpha and inputStr[i-1].isdigit:
            print()

alphaCount('12a3b2g')
alphaCount2('1a2b3g')