import random


class AverageGenerator:
    def __init__(self, list_size=0, min_value=1, max_value=100):
        self.list_size = list_size
        self.max_value = max_value
        self.min_value = min_value
        self.new_list = []
        self.average = 0
        self.list_generator()
        self.find_average_checker()
        self.find_average()

    def list_generator(self):
        self.new_list = [random.randint(self.min_value, self.max_value) for i in range(self.list_size)]

    def find_average(self):
        self.average = self.new_list[0] if len(self.new_list) == 1 else sum(self.new_list) / len(self.new_list)

    def find_average_checker(self):
        self.find_average_empty_error()
        self.find_average_type_error()
        self.find_average_size_error()

    def find_average_type_error(self):
        if not isinstance(self.new_list, list):
            raise TypeError("Input should be a list.")

    def find_average_empty_error(self):
        if not self.new_list:
            raise ValueError("List is empty.")

    def find_average_size_error(self):
        if len(self.new_list) < 2:
            raise ValueError("List size less than 2 items.")

    def __str__(self):
        return f'Среднее арифметическое списка {self.new_list} \nравно {self.average}'


class AverageComparator:
    @staticmethod
    def avg_compare(first_avg, second_avg):
        if first_avg > second_avg:
            return 'First average is gross than second.'
        elif first_avg < second_avg:
            return 'First average is less than second.'
        else:
            return 'Averages are equal.'

