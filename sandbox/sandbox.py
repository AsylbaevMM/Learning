def writer_main(args):
    with open ('data.txt','a') as data:
        print(f'{"<word>".join(args)}', file = data)


def reader_main(word):
    with open ('data.txt','r') as data:
        list = data.read().split('\n')
        for i in list:
            if word in i:
                return i.split('<word>')