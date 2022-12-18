def reader_main(family):
    
    with open ('data.txt','r') as data:
        spis = []
        list = data.read().split('\n')

        flag = 0
        for i in range(len(list)):
            if family in list[i]:
                spis = list[i].split('<word>')
                #return spis #вывод 1 раз
                flag = 1

        if flag == 0:
            return None

        return spis