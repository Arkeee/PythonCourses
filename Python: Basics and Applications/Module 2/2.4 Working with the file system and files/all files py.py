"""
Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории,
в которых есть хотя бы один файл с расширением ".py".

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.

Для лучшего понимания формата задачи, ознакомьтесь с примером.
"""
import os
import os.path


paths = []

for curent_dir, dirs, files in os.walk(""):
    if ".py" in str(files):
        paths.append(curent_dir.replace("..\\", ""))
for elem in sorted(paths):
    print(elem)