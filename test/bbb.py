def parce_input(chars):                 # Модуль для обработки входных данных, избавляется от пробелов и выдает массив из операций, скобок и чисел 
    chars = chars.replace(' ', '')
    print(chars)
    result = []
    temp = ''
    for i in range(len(chars)): 
        
        if chars[i].isdigit() or (chars[i] == '-' and not chars[i-1].isdigit()):
            temp += chars[i]
            print(result)
        else:
            if temp.isdigit() or (temp.startswith('-') and len(temp)>1):
                result.append(int(temp))
            result.append(chars[i])
            temp = ''
            print(result)
    if len(temp) > 0:
        result.append(temp)
    return result


print(parce_input('5 * (6 + 3) / ( 30 / (6-4)) + 3'))