import json
import csv

def transform_csv_to_json():
    
    openfile = input("Input your file's name: ")
    
    with open(openfile) as f:
        reader = csv.reader(f)
        header_row = next(reader)
    
    json_list = []
    values = []
    
    n = 0
    while n < len(header_row):
        
        with open(openfile) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            value = [row[n] for row in reader]
            values.append(value)
            n += 1
            
    for index, column_header in enumerate(header_row):
        print(index, column_header)
            
    m = 0
    while m < len(value):
        
        n = 0
        dict = {}
        while n < len(header_row):
            k = header_row[n]
            v = values[n]
            dict[k] = v[m]
            n += 1
        json_list.append(dict)
        
        m += 1
        
    storefile = input("Store your file at: ")
    
    with open(storefile, 'w') as s:
        json.dump(json_list, s)
