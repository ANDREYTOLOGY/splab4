# Написать две программы.Первая – вычисляет контрольную сумму файла. Вторая –
# вычисляет контрольную сумму всех файлов в директории, при этом обработка каждого
# отдельного файла осуществляется с помощью первой программы в отдельном процессе.

import json
import subprocess
import os
import hashlib

def hash_string(string): # получаем хэш от строки
	h = hashlib.new('md5') 
	h.update(string.encode()) 
	return h.hexdigest() 


path = '.'  # директория, в которой будем смотреть файлы. Точка значит, что в директории где находится исходный файл

processes = []  # массив, в котором мы будем хранить дескрипторы от запущенных процессов

files = os.listdir(path)  # смотрим файлы по нужному пути
for file in files:  # для каждого файла в директории
	fullpath = os.path.join(path, file)  # получаем его полный путь
	if os.path.isdir(fullpath): # проверяем - является ли файл директорией?
		continue  # если да - он нам не нужен, пропускаем

	print(f'{fullpath} found')  # иначе пишем что обрабатываем

	process = subprocess.Popen(  # запускаем процесс
		["python3", "hasher.py", fullpath],  # fullpath станет 2ым аргументом в вызванной программе
		stdout=subprocess.PIPE
	)
	processes.append(process)  # запоминаем созданный дескриптор

result = []  # создаем переменную, в которую сложим хэши от файла

for process in processes:  # для каждого процесса
	process.wait()  # ждем окончания процесса
	out, err = process.communicate()  # получаем то, что процесс писал в stdout и stderr
	data = out.decode()  # декодируем то, что он отправил в stdout
	result.append(data)  # добавляем результат

# собираем все хэши в одну большую строку, которую хэшим, после чего итоговый хэш выводим на экран
print(hash_string(''.join(result)))
