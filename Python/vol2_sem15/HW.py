import logging
import argparse

logging.basicConfig(level=logging.INFO, filename="loger.log", filemode="a",
            format='%(levelname)s, %(asctime)s, %(message)s')


def roman_to_dec(num):
    rome = num
    d = {'CM':900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4,'M':1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    
    total = 0
    while rome:
        flag = True
        for i in d:
            if rome.startswith(i):
                flag = False
                total += d[i]
                rome = rome.replace(i, '', 1)
                break
        if flag:
            logging.error(f'{num} is not an roman number')
            raise ValueError
    logging.info(f"Roman {num} is decimal {total}")
    return total



parser = argparse.ArgumentParser(description='Roman numbers to decimal')
parser.add_argument('-r', '--roman_number', type=str, default='', help='Input roman number')
num = parser.parse_args().roman_number
if not num:
    num = input('Input roman number >>> ')
try:
    print(f'Roman {num} is decimal {roman_to_dec(num)}')
except:
    print(f"{num} is not roman number")


# Для запуска с аргументами: -r MMCF
