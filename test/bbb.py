shifr = input()
sdv = int(input())

for i in shifr:
    if 97 <= ord(i) <= 122:
        temp =ord(i) + sdv
        if temp > 122:
            temp -= 26
      
        print(chr(temp), end = "")
    elif 65 <= ord(i) <= 90:
        temp =ord(i) + sdv
        if temp >90:
            temp -= 26
        
        print(chr(temp), end = "")
    else:
        print(i, end = '')