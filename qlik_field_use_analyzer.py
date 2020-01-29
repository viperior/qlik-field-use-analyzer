import json, os, re

def analyze_logs(qlik_script_directory='./input/Script/', log_analysis_output_path='./output/log_analysis_results.json', write_analysis_to_file=False):
    log_analysis_results = []
    
    for file_name in os.listdir(qlik_script_directory):
        current_file_log_analysis_results = {}
        file_number = 1
        current_file_metadata = {}
        current_file_metadata['file_number'] = file_number
        current_file_metadata['file_directory'] = qlik_script_directory
        current_file_metadata['file_name'] = file_name
        current_file_metadata['file_path'] = current_file_metadata['file_directory'] + current_file_metadata['file_name']
        current_file_log_analysis_results['file_metadata'] = current_file_metadata
        current_file_load_statements = []
        
        with open(current_file_metadata['file_path'], 'r') as file:
            line_number = 1
            current_load_statement = {}
            current_load_statement['statement_description'] = 'Load statement'
            
            for line in file:
                if line_is_start_of_new_load_statement(line):
                    current_load_statement['start_line_number'] = line_number
                     
                if line_is_load_statement_confirmation(line):
                    current_load_statement['end_line_number'] = line_number - 1
                    current_file_load_statements.append(current_load_statement)
                    current_load_statement = {}
                    
                line_number += 1
        
        current_file_log_analysis_results['load_statement_line_ranges'] = current_file_load_statements
        log_analysis_results.append(current_file_log_analysis_results)
        file_number += 1
    
    log_analysis_results_json = json.dumps(log_analysis_results)
    
    if write_analysis_to_file:
        with open(log_analysis_output_path, 'w') as output_file:
            output_file.write(log_analysis_results_json)
    
def line_is_load_statement_confirmation(line):
    return pattern_appears_in_text(r'loaded:', line, ignore_case=True)

def line_is_start_of_new_load_statement(line):
    return pattern_appears_in_text(r'\s+load\s+', line, ignore_case=True)
    
def pattern_appears_in_text(regex_pattern, text, ignore_case=False):
    if ignore_case:
        matches = re.findall(regex_pattern, text, re.IGNORECASE)
    else:
        matches = re.findall(regex_pattern, text)
        
    return len(matches) > 0

analyze_logs(log_analysis_output_path='./output/log_analysis_results-sample.json', write_analysis_to_file = True)
