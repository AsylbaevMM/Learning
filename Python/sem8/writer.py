def writer_main(args):
    with open ('data.txt','a') as data:
        list= ' '.join(map(str,args)) + ' 1\n'  
        data.write(list)
        