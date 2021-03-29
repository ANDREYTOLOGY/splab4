import sys
import hashlib

def hash_file(path): 
	h = hashlib.new('md5')  
	with open(path, 'rb') as f:  
		while True: 
			block = f.read(1024) 
			if not block:  
				break 
			h.update(block) 
	
	return h.hexdigest()  

if __name__ == '__main__':
	filepath = sys.argv[1] 
	print(hash_file(filepath)) 
