import os

def open_file(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            r = f.read()
    else:
        with open("file.txt", "w") as f:
            for i in range(10):
                f.write(str(i) + '\n')

path =r'C:\Users\PC\PycharmProjects\HelloWord\python2023\pythonKurs\intermediateLevel\file_opeartions\file.txt'


open_file(path)

print(os.path.isfile(path))



