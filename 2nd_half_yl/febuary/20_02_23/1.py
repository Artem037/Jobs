from os import listdir, getcwd, path
from os.path import isfile, join


def human_read_format(size):
    if size >= 1024:
        size_kb = round(size / 1024)
        if size_kb >= 1024:
            size_mb = round(size_kb / 1024)
            if size_mb >= 1024:
                size_gb = round(size_mb / 1024)
                return f'{size_gb}ГБ'
            return f'{size_mb}МБ'
        return f'{size_kb}КБ'
    return f'{size}Б'


def get_files_sizes():
    mypath = getcwd()
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    data = []
    for i in onlyfiles:
        data.append(f'{i} {human_read_format(path.getsize(i))}')
    return '\n'.join(data)


print(get_files_sizes())