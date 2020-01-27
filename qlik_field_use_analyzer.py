import os, re

input_file_directory = './input/Script/'
load_keyword_regex_pattern = r'\s+load\s+'
loaded_fields_confirmation_regex_pattern = r'loaded:'

for file_name in os.listdir(input_file_directory):
    file_number = 1
    current_file_path = input_file_directory + file_name
    
    with open(current_file_path, 'r') as file:
        line_number = 1
        
        for line in file:
            matches = re.findall(load_keyword_regex_pattern, line, re.IGNORECASE)
            
            if len(matches) > 0:
                 print(matches)
                 print(line)
                 
            matches = re.findall(loaded_fields_confirmation_regex_pattern, line, re.IGNORECASE)
            
            if len(matches) > 0:
                print(matches)
                print(line)
                
        line_number += 1
                
    file_number += 1
