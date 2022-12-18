def writer_main(args):
    with open ('data.txt','a') as data:
        list= '<word>'.join(map(str,args)) + '\n'  
        data.write(list)
        