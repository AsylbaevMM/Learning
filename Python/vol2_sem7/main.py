# ✔Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔расширение 
# ✔минимальная длина случайно сгенерированного имени, по умолчанию 6 
# ✔максимальная длина случайно сгенерированного имени, по умолчанию 30 
# ✔минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔максимальное число случайных байт, записанных в файл, по умолчанию 4096 
# ✔количество файлов, по умолчанию 42 
# ✔Имя файла и его размер должны быть в рамках переданного диапазона.
from string import ascii_letters
from random import randint, sample, randbytes, choice
import os
from re import findall
from time import sleep


def makefile(extention, smallest=6, largest=30, min_bytes=256, max_bytes=4096, count=42):
    names = set()
    while len(names) < count:
        names.add(''.join(sample(ascii_letters, randint(smallest, largest))))

    for name in names:
        with open(f'{name}.{extention}', 'wb') as file:
            temp = randbytes(randint(min_bytes, max_bytes))
            file.write(temp)
            print(len(temp))



def makefiles(**extentions):
    for extention, count in extentions.items():
        makefile(extention=extention,  count=count)

def makefile_topath(path, extention):
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    makefile(extention)

def replace_files():
    for file in os.listdir():
        extention = file.split('.')[-1]
        if not os.path.exists(extention):
            os.mkdir(extention)
        os.replace(file, os.path.join(os.getcwd(), extention, file))




############## homework ################

def rename_files(new_name='', nums_count=3, old_extention='', new_extention='', name_slice=None, ):
    # делаем проверку на диапазон сохраняемого имени
    if name_slice and len(findall(r'\d+', str(name_slice))) > 3:
        raise ValueError('Неверные аргументы в диапазоне сохраняемого оригинального имени')
    count = 1
    oldname_part = ''
    for file in os.listdir():
        # проверка, если задано старое расширение файла, пропускаем все неподходящие
        if old_extention and file.split('.')[-1] != old_extention:
            continue
        # если задан диапазон сохраняемого имени вытаскиваем его переводя строку name_slice в slice-объект
        if name_slice:
            oldname_part = os.path.basename(file).rsplit('.')[0][slice(*[int(i) for i in findall(r'\d+', str(name_slice))])]
        # набиваем в номер нули до получения нужного размера
        number = str(count).rjust(nums_count, '0')
        # ставим в расширение новое расширение, если оно не пустое, иначе берем старое
        result_extention = new_extention or file.split('.')[-1]
        # переименовываем файл и увеличиваем счетчик файлов
        os.rename(file, f"{oldname_part}{new_name}{number}.{result_extention}")
        count += 1


if __name__ == "__main__":
    # создание случайных файлов
    makefiles(mp3 = 10, txt=5, torrent= 5)
    sleep(10)

    # переименование txt файлов с изменением расширения и сохранением диапазона старого имени
    rename_files('test', old_extention='txt', new_extention='word', name_slice=[2, 5])
    sleep(10)

    # переименование всех файлов с сохранением старого расширения без сохранения диапазона старого имени
    rename_files('test1')
