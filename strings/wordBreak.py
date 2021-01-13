def wordBreak(inputStr, dictWords, out=""):
    n = len(inputStr)
    strlist = []

    if not inputStr:
        print(out)
        return
    
    for i in range(1, n+1):
        prefix = inputStr[:i]

        if prefix in dictWords:
            wordBreak(inputStr[i:], dictWords, out + " " + prefix )

wordBreak('carsgofast', ['this', 'are', 'cars', 'the', 'go', 'fast'])
