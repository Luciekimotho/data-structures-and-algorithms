def repeatedString(s, n):
    num = 0

    for a in s:
        if a == 'a':
            num += 1
    print(num)  

    times = n // len(s)
    rem = n % len(s) 
    
    remTimes = 0
    
    for i in range(0, rem):
        if s[i] == 'a':
            remTimes += 1
    
    print(remTimes)

    num = (num * times) + remTimes   
    print(num)   
    return num


repeatedString('epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq', 549382313570)