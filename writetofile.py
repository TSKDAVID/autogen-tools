def writetofile(filename: str, text: str) -> str:
    script_directory = os.path.dirname(__file__)
    file_path = os.path.join(script_directory, filename)
    with open(file_path, 'w') as file:
        file.write(f"\n{text}")
    return f"Text appended successfully to {file_path}"


#unlike appender tool this one erases everything that was written in a file and adds a new text and just as appender takes 2 arguments filename or path and text that must be written
