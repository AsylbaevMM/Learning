def calcul(value,  bytes):
    if bytes == 'B':
        return int(value)
    elif bytes == "KB":
        return int(value) * 1024
    elif bytes == 'MB':
        return int(value) * 1024 * 1024
    elif bytes == 'GB':
        return int(value) * 1024 * 1024 * 1024

def keysort(args):
    return args[1]

sizes = ["B", "KB", 'MB', "GB"]

with open(r"C:\Users\asylb\OneDrive\Рабочий стол\files.txt", 'r', encoding= 'UTF-8') as file:
    data = list(map(str.strip, file.readlines()))
    file_types = set()
    for i in range(len(data)):
        data[i] = data[i].replace('.', ' ')
        data[i] = data[i].split()
        data[i][2] = calcul(data[i][2], data[i][3])
        file_types.add(data[i][1])
    data.sort(key = keysort)
    file_types = list(sorted(file_types))
    for i in file_types:
        total = 0
        temp = []
        for j in data:
            if j[1] == i:
                temp.append(f'{j[0]}.{j[1]}')
                total += j[2]
        print(*sorted(temp), sep = '\n')        
        counts = 0
        while total > 1024:
            total = round(total/1024) 
            counts += 1
        print('-'*10)
        print(f"Summary: {int(total)} {sizes[counts]}")
        print()