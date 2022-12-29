from datetime import datetime 
def log_writer(string):
    with open ('output.txt','a') as output_file:
        data = datetime.now().strftime('Year:%Y Month:%m Day:%d Hour:%H Minute:%M Second:%S  ')
        output_file.writelines(f'{data} {string}\n')

def log_reader():
    with open ('output.txt','r') as file:
        data = file.read()
    return data



