def log_reader():
    with open ('output.txt','r') as file:
        data = file.read()
    return data

print(log_reader())