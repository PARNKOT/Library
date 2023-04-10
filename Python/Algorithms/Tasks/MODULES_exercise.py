#!/usr/bin/python3

import optparse
import os
import datetime

class FileInfo:
	def __init__(self, filename=''):
		self.name = filename
		self.datetime_file = ''
		self.size = ''
		self.Title = ''
	
	def __repr__(self):
		str_date = str(self.datetime_file)
		str_size = str(self.size)
		str_return = ''
		if str_date:
			str_return += str_date + '\t'
		if str_size:
			str_return += str_size + '\t'
		str_return += self.name
		return str_return	

def parseOptions():
    parser = optparse.OptionParser()
    #parser.add_option("-h", "--help")
    parser.add_option("-H", "--hidden", action="store_true", dest="isHidden", help="Show hidden folders")
    parser.add_option("-m", "--modified", action="store_true", dest="isModified")
    parser.add_option("-o", "--order", dest="ORDER", type='str', help="Set out order")
    parser.add_option("-r", "--recursive", action="store_true", dest="isRecursive")
    parser.add_option("-s", "--sizes", action="store_true", dest="isSize")
    parser.set_defaults(ORDER='name')
    return parser.parse_args()

def make_file_info(opts, file='', isTitle=False) -> FileInfo:
	fileinfo = FileInfo(file)
	if bool(opts.isModified):
		if isTitle:
			fileinfo.Title += "Last modified:\t\t"
		else:
			fileinfo.datetime_file = datetime.datetime.fromtimestamp(int(os.path.getmtime(file)))
	if bool(opts.isSize):
		if isTitle:
			fileinfo.Title += "Size:\t"  
		else:
			fileinfo.size = os.path.getsize(file)
	if isTitle:
		fileinfo.Title += "Name:"
	
	return fileinfo

def main():
	opts, args = parseOptions()	

	if not args:
		args = ['.']

	title = make_file_info(opts, isTitle=True)
	print(title.Title + '\n')

	file_list = list()

	if bool(opts.isRecursive):
		for dir, dirs, files in os.walk(args[0]):
			for file in files:			
				if not bool(opts.isHidden) and file.startswith('.'):
					continue
				else:			
					file_list.append(make_file_info(opts, dir[2:]+'/'+file))
	else:
		for file in os.listdir(args[0]):
			if not bool(opts.isHidden) and file.startswith('.'):
				continue
			else:			
				file_list.append(make_file_info(opts, file))
	
	order_dict = {'n':'name', 's':'size', 'd':'datetime_file'}
	file_list = sorted(file_list, key=lambda fileinfo: getattr(fileinfo, order_dict[opts.ORDER.lower()[0]]))
	
	for file in file_list:
		print(file)

	
	#print(os.listdir(args[0]))
	#files_list = list()
	
	#for file in 

if __name__ == "__main__":
	main()
