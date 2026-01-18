import os

def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print('File not found!')
        return None

def write_file(file_path, content):
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        except Exception as e:
            print('Error writing to file:', e)
