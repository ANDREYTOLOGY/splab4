import sys
import hashlib

def hash_file(path): # получение хэша от файла
	h = hashlib.new('md5')  # создаем хэшер
	with open(path, 'rb') as f:  # открываем файл на чтение по байтам
		while True: 
			block = f.read(1024) # читаем кусками по 1024 байта
			if not block:  # если файл кончился - выходим
				break 
			h.update(block) # хэшируем
	
	return h.hexdigest()  # возвращаем хэш в виде hex-значений

if __name__ == '__main__':
	filepath = sys.argv[1] # взятие второго аргумента командной строки (пути к файлу)
	print(hash_file(filepath)) # вывод в консоль результата хэширования содержимого файла
