def reader_main(family):
   with open ('data.txt','r') as data:
        list = data.read().split(' 1')
        for i in range(len(list)):
            if family not in list:
                spis = list[i].split()
                return spis 


