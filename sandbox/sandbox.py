def change_name(file_name, ch_name):
    data=open(file_name,'r')
    list_name=list()
    for line in data:
        if ch_name in line:
            new_name=input("Введите новеое ФИО и номер телефона:")
            list_name.append(new_name+"\n")
            continue
        list_name.append(line)
    data.close()
    list_name=list(filter(lambda x:x !="",list_name))
    data=open(file_name,'w')
    for item in list_name:
        data.write(item)
    data.close()
    print()