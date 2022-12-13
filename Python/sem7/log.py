from datetime import datetime 
def log_main(string):
    with open ('output.txt','r+') as output_file:
        output_file.write(datetime.now().strftime('Year:%Y Month:%m Dayь:%d Hour:%H Minute:%M Second:%S\n'))
        output_file.write('string') 