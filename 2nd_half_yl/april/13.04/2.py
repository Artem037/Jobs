from zipfile import ZipFile


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


with ZipFile('input.zip') as myzip:
    files_info = myzip.infolist()
    for name in myzip.namelist():
        items = name.rstrip("/").split("/")
        if name[-1] != '/':
            print("  " * (len(items) - 1) + items[-1] + human_read_format(
                files_info[myzip.namelist().index(name)].file_size))
        else:
            print("  " * (len(items) - 1) + items[-1])
