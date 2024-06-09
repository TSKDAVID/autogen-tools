def appender(filename: str, text: str) -> str:
    script_directory = os.path.dirname(__file__)
    file_path = os.path.join(script_directory, filename)
    with open(file_path, 'a') as file:
        file.write(f"\n{text}")
    return f"Text appended successfully to {file_path}"

#this code simply appends text to file and receives 2 arguments filename or path and text that needs to be appended
