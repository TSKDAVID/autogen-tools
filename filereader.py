def read_file_skip_leading_blank_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Skip leading blank lines
    text_started = False
    content = []
    
    for line in lines:
        if not text_started and line.strip() == '':
            continue
        text_started = True
        content.append(line)
    
    return ''.join(content)
