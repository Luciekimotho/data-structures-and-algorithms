def reverse(sentence):
    word = ''
    arr = []
    n = len(sentence)

    for i, char in enumerate(sentence):   #Splitting method
        if  i == n-1:
            word = word + char
            arr.append(word)
        elif char !=  ' ':
            word = word + char
        else: 
            arr.append(word)
            word = ''
    # print(arr)

    words = sentence.split(' ')
    n = len(words)
    for i in range(n // 2):
        words[i], words[n-i-1] = words[n-i-1], words[i]

    #print(words)

    print(' '.join(arr[::-1]))
    return ' '.join(arr[::-1])





reverse('I am a girl')