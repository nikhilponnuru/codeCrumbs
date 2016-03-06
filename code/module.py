import os

def get_extension(file_name):
    if file_name.find('.')!=-1:

        ext = file_name.split('.')

        return (ext[1])
    else:

        return 'txt'


def cut(str, len1):
    return str[len1 + 1:]  #to remove first line which is meant for reading from which file



#for displaying contents
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
