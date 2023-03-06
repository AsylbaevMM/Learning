

class Loggable():
    def log(self, item):
        with open('log.txt', 'a', encoding = 'utf-8') as output_file:
            print(item, file=output_file)