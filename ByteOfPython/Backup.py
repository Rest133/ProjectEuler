import os
import time

# 1.Файлы и папки,которые необходимо скопировать хранятся в списке
source = "E:\\D\\University\\PyCharm Projects\\ProjectEuler\\ByteOfPython\\save_this"
# Двойные кавычки нужны для имён, содержащих пробелы
# 2.Резервные каталоги должны храниться в соседнем каталоге
target_dir = "E:\\D\\University\\PyCharm Projects\\ProjectEuler\\ByteOfPython\\Backup"

# 3.Файлы помещаются в zip-архив
# 4.Имя файла = текущий каталог + время
target = time.strftime('%Y%m%d') + '.rar'

# 5.Используем консольную команду для архивации
create_rar = "rar.exe a {0}".format(target)
copy_to_rar = "rar.exe m {0} {1}".format(target, source)
move_rar = "move E:\\D\\University\\PyCharm Projects\\ProjectEuler\\ByteOfPython\\{0} {1}".format(target, target_dir)
# 6.Проверка
print(create_rar)
print(copy_to_rar)
print(move_rar)

# 7.Запуска архивации
if os.system(create_rar) == 0:
    print("Архив создан")
else:
    print("Архивация прошла неудачно")
