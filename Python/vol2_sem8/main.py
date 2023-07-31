import os
import json
import csv
import pickle

def check_directory(directory, curent_dir=None):

    result = []
    
    def check_recursive(directory, parent = None):
        if parent is not None:
            directory = parent + '\\' + directory
        info_dict = {}
        info_list = []
        total_size = 0
        
        if os.path.isdir(directory):
            info_dict['a_type'] = 'directory'
            info_dict['childs'] = {}
            for obj in os.listdir(directory):
                info_dict['childs'][obj] = check_recursive(obj, f'{directory}')
                total_size += info_dict['childs'][obj]['b_size']
                info_list.append([directory, obj, info_dict['childs'][obj]['a_type'], info_dict['childs'][obj]['b_size']])
            info_dict['b_size'] = total_size
            
        else:
            info_dict['a_type'] = 'file' 
            info_dict['b_size'] = os.path.getsize(directory)
        nonlocal result
        print(info_list)
        result.extend(info_list)
        return info_dict
    
    result_dict = {directory: check_recursive(directory)}

    with open('result.json', 'w', encoding = 'utf-8') as json_file:
        json.dump(result_dict, json_file, ensure_ascii=False, indent=5, sort_keys=True)

    with open('result.csv', 'w', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['parent', 'obj', 'type', 'size'])
        writer.writerows(result)

    with open('result.pkl', 'wb') as pickle_file:
        pickle.dump(result, pickle_file)


check_directory(r'C:\Users\asylb\OneDrive\Рабочий стол\Learning\Python\vol2_sem8')
