

def re_writer(in_file, out_file):
    with (
        open(in_file, mode = 'r', encoding = 'utf-8') as input_file,
        open(out_file, mode = 'w', encoding = 'utf-8') as output_file
    ):
      output_file.write(input_file.read())



re_writer(r'C:\Users\asylb\OneDrive\Рабочий стол\Learning\errors\lesson3\in_test.txt', r'C:\Users\asylb\OneDrive\Рабочий стол\Learning\errors\lesson3\out_test.txt')  
        