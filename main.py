# Написать две программы.Первая – вычисляет контрольную сумму файла. Вторая –
# вычисляет контрольную сумму всех файлов в директории, при этом обработка каждого
# отдельного файла осуществляется с помощью первой программы в отдельном процессе.

import json
import subprocess
import os
import hashlib

def hash_string(string): 
	h = hashlib.new('md5') 
	h.update(string.encode()) 
	return h.hexdigest() 


path = '.'  

processes = []  
files = os.listdir(path)  
for file in files:  
	fullpath = os.path.join(path, file)  
	if os.path.isdir(fullpath):
		continue  

	print(f'{fullpath} found')  

	process = subprocess.Popen(  
		["python3", "hasher.py", fullpath],  
		stdout=subprocess.PIPE
	)
	processes.append(process)  

result = []  

for process in processes:  
	process.wait() 
	out, err = process.communicate()  
	data = out.decode()  
	result.append(data)  

print(hash_string(''.join(result)))
