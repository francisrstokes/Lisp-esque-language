import os

def read_file(file_name):
	read_data = None
	try:
		with open(file_name, "r+b") as f:
			read_data = f.read().decode("utf-8") 
	except:
		raise Exception("Couldn't read the file. Please check the filename and the path.")
	return read_data

def get_real_dir_name(file):
	return os.path.dirname(os.path.realpath(file))

def is_int(a):
	return a % 1 == 0
