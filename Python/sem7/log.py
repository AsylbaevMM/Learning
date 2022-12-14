from datetime import datetime 
def log_main(string):
    with open ('output.txt','a') as output_file:
        output_file.write(datetime.now().strftime('Year:%Y Month:%m Day:%d Hour:%H Minute:%M Second:%S')+string)