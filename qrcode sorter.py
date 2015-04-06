import subprocess
import os
import locale
import glob
encoding = locale.getdefaultlocale()[1]

def get_code(file):
	# if there is no QR code in the image, or if for some reason zbar can't read the code
	# then it will throw an error, so I use try/except to handle that error gracefully
	# images like this will be put in a folder called "unreadable_code"
	try:
		raw_code = subprocess.check_output(["C:\\Program Files (x86)\\ZBar\\bin\\zbarimg", "-q", \
		file])
		#print(raw_code)
		raw_code = raw_code.rstrip()
		raw_code = raw_code.decode(encoding)
		code = raw_code.split(':',1)[1]
		return(code)
	except:
		return("unreadable_code")

def make_folder(folder_name):
 folder = os.path.join(os.getcwd(), folder_name)
 #print(folder)
 os.makedirs(folder, exist_ok=True)


#test =  "G:\\Dropbox\\Research Organized\\Projects\\03.misc small other\\3.3 barcodes\\20150320_0474.JPG"
#print(get_code(test))

#print(os.listdir())

image_files=glob.glob('*.JPG') + glob.glob('*.png')
print(image_files)

for file in image_files:
 # make the file into a path
 file_path = os.path.join(os.getcwd(), file) 
 # get the code
 code = get_code(file)
 # make the folder
 folder = os.path.join(os.getcwd(), code)
 #print(folder)
 os.makedirs(folder, exist_ok=True)
 #move the file
 os.rename(file_path, folder + "\\" + file)
 #done
