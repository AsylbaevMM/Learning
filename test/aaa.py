with open(r"C:\Users\asylb\OneDrive\Рабочий стол\Learning\test\data.txt", 'r', encoding='utf-8') as input_file:
    data = list(map(str.strip, input_file.readlines()))
    
    uncommented_methods = []
    for i in range(len(data)):
        
        if data[i].startswith('def ') and not data[i-1].startswith('#'):
            uncommented_methods.append(data[i])
    uncommented_methods = list(map(lambda x: x[4:x.find('(')], uncommented_methods))
    if len(uncommented_methods) == 0:
        print('Best Programming Team')
    else:
        print(*uncommented_methods, sep = '\n')