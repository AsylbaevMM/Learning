def reader_main(family):
    
    with open ('data.txt','r') as data:
        result = []
        spis = []
        list = data.read().split('\n')

        for i in range(len(list)):
            if family.lower() in list[i].lower():
                spis = list[i].split('<word>')
                result.append(spis)
               
        return result   
#print(reader_main('Иванов'))

