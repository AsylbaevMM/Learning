def reader_main(family):
    with open ('data.txt','r') as data:
        list = data.read().split('<string>\n')
        for i in range(len(list)):
            if family in list[i]:
                spis = list[i].split("<word>")
                return spis
            else:
                print('Введены не корректные данные в поиске')
                break  

print(reader_main('Иванов'))