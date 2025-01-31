def read_file(file_path: str):
    with open(file_path, 'rb') as file:
        return file.read()

def write_file(file_path: str, data):
    with open(file_path, 'w', encoding='cp1252') as file:
        file.write(data)
